export default defineNuxtRouteMiddleware((to, from) => {
  const authStore = useAuthStore()

  // Инициализируем store из localStorage
  authStore.init()

  // Если пользователь авторизован, редиректим на главную
  if (authStore.isAuthenticated) {
    return navigateTo('/')
  }
})

