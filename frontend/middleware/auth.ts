export default defineNuxtRouteMiddleware((to, from) => {
  const authStore = useAuthStore()

  // Инициализируем store из localStorage
  authStore.init()

  // Если пользователь не авторизован и пытается зайти на защищённую страницу
  if (!authStore.isAuthenticated && to.path !== '/login') {
    return navigateTo('/login')
  }

  // Если пользователь авторизован и пытается зайти на страницу логина
  if (authStore.isAuthenticated && to.path === '/login') {
    return navigateTo('/')
  }
})

