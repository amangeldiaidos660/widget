<template>
  <div class="container">
    <div class="row justify-content-center align-items-center min-vh-100">
      <div class="col-md-5 col-lg-4">
        <div class="card shadow">
          <div class="card-body p-5">
            <div class="text-center mb-4">
              <h2 class="card-title">Вход в портал</h2>
              <p class="text-muted">Введите данные для входа</p>
            </div>

            <form @submit.prevent="handleLogin">
              <div v-if="error" class="alert alert-danger" role="alert">
                {{ error }}
              </div>

              <div class="mb-3">
                <label for="username" class="form-label">Логин</label>
                <input
                  id="username"
                  v-model="username"
                  type="text"
                  class="form-control"
                  :class="{ 'is-invalid': errors.username }"
                  placeholder="Введите логин"
                  required
                  autocomplete="username"
                />
                <div v-if="errors.username" class="invalid-feedback">
                  {{ errors.username }}
                </div>
              </div>

              <div class="mb-4">
                <label for="password" class="form-label">Пароль</label>
                <input
                  id="password"
                  v-model="password"
                  type="password"
                  class="form-control"
                  :class="{ 'is-invalid': errors.password }"
                  placeholder="Введите пароль"
                  required
                  autocomplete="current-password"
                />
                <div v-if="errors.password" class="invalid-feedback">
                  {{ errors.password }}
                </div>
              </div>

              <button
                type="submit"
                class="btn btn-primary w-100"
                :disabled="loading"
              >
                <span
                  v-if="loading"
                  class="spinner-border spinner-border-sm me-2"
                  role="status"
                  aria-hidden="true"
                ></span>
                {{ loading ? 'Вход...' : 'Войти' }}
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: false,
  middleware: 'guest'
})

const authStore = useAuthStore()
const router = useRouter()

const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')
const errors = ref<{ username?: string; password?: string }>({})

const handleLogin = async () => {
  error.value = ''
  errors.value = {}
  loading.value = true

  try {
    const result = await authStore.login(username.value, password.value)

    if (result.success) {
      await router.push('/')
    } else {
      error.value = result.error || 'Неверный логин или пароль'
    }
  } catch (err: any) {
    error.value = err.message || 'Произошла ошибка при входе'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.min-vh-100 {
  min-height: 100vh;
}
</style>

