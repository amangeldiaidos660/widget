<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container-fluid">
      <NuxtLink to="/" class="navbar-brand">
        Портал заявок
      </NuxtLink>
      
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#portalNavbar"
        aria-controls="portalNavbar"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div id="portalNavbar" class="collapse navbar-collapse">
        <ul class="navbar-nav ms-auto align-items-center">
          <li class="nav-item dropdown me-2">
            <a
              class="nav-link dropdown-toggle text-white"
              href="#"
              id="userDropdown"
              role="button"
              data-bs-toggle="dropdown"
              data-bs-auto-close="true"
              aria-expanded="false"
            >
              {{ authStore.user?.username || 'Пользователь' }}
            </a>
            <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="userDropdown">
              <li>
                <a class="dropdown-item" href="#" @click.prevent="handleLogout">
                  Выход
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <button 
              class="btn btn-outline-light btn-sm" 
              @click="handleLogout"
              type="button"
            >
              Выход
            </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
const authStore = useAuthStore()
const router = useRouter()

const handleLogout = async () => {
  authStore.logout()
  await router.push('/login')
}
</script>

<style scoped>
.navbar-brand {
  font-weight: 600;
}
</style>

