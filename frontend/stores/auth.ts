import { defineStore } from 'pinia'
import * as authApi from '~/api/auth'

interface User {
  id: number
  username: string
  email?: string
  first_name?: string
  last_name?: string
}

interface AuthState {
  user: User | null
  token: string | null
  refreshToken: string | null
  isAuthenticated: boolean
}

export const useAuthStore = defineStore('auth', {
  state: (): AuthState => ({
    user: null,
    token: null,
    refreshToken: null,
    isAuthenticated: false
  }),

  getters: {
    isLoggedIn: (state) => state.isAuthenticated && state.token !== null
  },

  actions: {
    // Инициализация из localStorage
    init() {
      if (process.client) {
        const token = localStorage.getItem('auth_token')
        const refreshToken = localStorage.getItem('auth_refresh_token')
        const userStr = localStorage.getItem('auth_user')
        
        if (token && userStr) {
          this.token = token
          this.refreshToken = refreshToken
          this.user = JSON.parse(userStr)
          this.isAuthenticated = true
        }
      }
    },

    // Вход в систему
    async login(username: string, password: string) {
      try {
        const response = await authApi.login(username, password)

        this.token = response.access
        this.refreshToken = response.refresh

        // Получаем информацию о пользователе через защищённый эндпоинт
        await this.fetchUser()

        // Сохраняем в localStorage
        if (process.client) {
          localStorage.setItem('auth_token', this.token)
          if (this.refreshToken) {
            localStorage.setItem('auth_refresh_token', this.refreshToken)
          }
          if (this.user) {
            localStorage.setItem('auth_user', JSON.stringify(this.user))
          }
        }

        this.isAuthenticated = true
        return { success: true }
      } catch (error: any) {
        console.error('Login error:', error)
        return { 
          success: false, 
          error: error.message || 'Ошибка входа' 
        }
      }
    },

    // Получение информации о пользователе
    async fetchUser() {
      if (!this.token) return

      try {
        const user = await authApi.getCurrentUser(this.token)
        this.user = user
        
        if (process.client) {
          localStorage.setItem('auth_user', JSON.stringify(user))
        }
      } catch (error) {
        console.error('Fetch user error:', error)
        // Если не удалось получить пользователя, пробуем через токен
        // В реальном приложении здесь может быть декодирование JWT
      }
    },

    // Проверка токена
    async checkToken() {
      if (!this.token) {
        this.init()
      }

      if (!this.token) {
        this.logout()
        return false
      }

      // Проверяем токен, делая запрос к защищённому эндпоинту
      try {
        const isValid = await authApi.validateToken(this.token)
        if (!isValid && this.refreshToken) {
          // Если токен невалиден, пробуем обновить
          return await this.refreshAccessToken()
        }
        return isValid
      } catch (error: any) {
        // Если токен невалиден, пробуем обновить
        if (this.refreshToken) {
          return await this.refreshAccessToken()
        }
        this.logout()
        return false
      }
    },

    // Обновление access токена
    async refreshAccessToken() {
      if (!this.refreshToken) {
        this.logout()
        return false
      }

      try {
        const response = await authApi.refreshToken(this.refreshToken)

        this.token = response.access
        
        if (process.client) {
          localStorage.setItem('auth_token', this.token)
        }

        return true
      } catch (error) {
        console.error('Refresh token error:', error)
        this.logout()
        return false
      }
    },

    // Выход из системы
    logout() {
      this.user = null
      this.token = null
      this.refreshToken = null
      this.isAuthenticated = false

      if (process.client) {
        localStorage.removeItem('auth_token')
        localStorage.removeItem('auth_refresh_token')
        localStorage.removeItem('auth_user')
      }
    }
  }
})

