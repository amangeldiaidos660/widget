<template>
  <div>
    <NuxtRouteAnnouncer />
    <NuxtPage />
  </div>
</template>

<script setup lang="ts">
const authStore = useAuthStore()

// Инициализируем store при старте приложения
onMounted(() => {
  authStore.init()
  // Проверяем токен при загрузке
  if (authStore.token) {
    authStore.checkToken()
  }
})
</script>

