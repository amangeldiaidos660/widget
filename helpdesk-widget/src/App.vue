<script setup>
import { computed } from 'vue'
import Auth from './components/Auth.vue'
import AdminPanel from './components/AdminPanel.vue'
import state from './stores/auth'

const isAuth = computed(() => state.isAuthenticated)
</script>

<template>
  <div class="app-inner container-fluid">
    <header class="mb-3 text-center">
      <h2>Helpdesk Widget — Панель управления</h2>
    </header>

    <component :is="isAuth ? AdminPanel : Auth" />
  </div>
</template>

<style scoped>
.app-inner { max-width: 960px; margin: 0 auto; }
</style>
