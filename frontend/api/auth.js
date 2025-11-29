import { API_ENDPOINTS } from './backendEndpoints.js'

/**
 * Получение JWT токенов (access + refresh)
 * @param {string} username - Логин пользователя
 * @param {string} password - Пароль пользователя
 * @returns {Promise<{access: string, refresh: string}>}
 */
export async function login(username, password) {
  const res = await fetch(API_ENDPOINTS.token, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, password }),
  })

  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Ошибка входа' }))
    throw new Error(error.detail || error.message || 'Неверный логин или пароль')
  }

  return await res.json()
}

/**
 * Обновление access токена
 * @param {string} refreshToken - Refresh токен
 * @returns {Promise<{access: string}>}
 */
export async function refreshToken(refreshToken) {
  const res = await fetch(API_ENDPOINTS.tokenRefresh, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ refresh: refreshToken }),
  })

  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Ошибка обновления токена' }))
    throw new Error(error.detail || error.message || 'Не удалось обновить токен')
  }

  return await res.json()
}

/**
 * Получение информации о текущем пользователе
 * @param {string} accessToken - Access токен
 * @returns {Promise<{id: number, username: string, email?: string}>}
 */
export async function getCurrentUser(accessToken) {
  const res = await fetch(API_ENDPOINTS.currentUser, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json',
    },
  })

  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: 'Ошибка получения пользователя' }))
    throw new Error(error.detail || error.message || 'Не удалось получить информацию о пользователе')
  }

  return await res.json()
}

/**
 * Проверка валидности токена (делает запрос к защищённому эндпоинту)
 * @param {string} accessToken - Access токен
 * @returns {Promise<boolean>}
 */
export async function validateToken(accessToken) {
  try {
    const res = await fetch(`${API_ENDPOINTS.tickets}?limit=1`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json',
      },
    })
    return res.ok
  } catch {
    return false
  }
}

