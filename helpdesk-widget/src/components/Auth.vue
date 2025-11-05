<script setup>
import { ref } from 'vue'
import { createUser, verifyUser, hashPassword, getUserByUsername } from '../services/db'
import state, { setUser } from '../stores/auth'

const tab = ref('login') // 'login' or 'register'

// Login fields
const loginUsername = ref('')
const loginPassword = ref('')
const loginError = ref('')
const loginSuccess = ref('')

// Register fields
const regUsername = ref('')
const regPassword = ref('')
const regError = ref('')
const regSuccess = ref('')

async function onLogin(e) {
  e.preventDefault()
  loginError.value = ''
  loginSuccess.value = ''
  if (!loginUsername.value || !loginPassword.value) {
    loginError.value = 'Введите имя пользователя и пароль.'
    return
  }
  const hash = await hashPassword(loginPassword.value)
  const ok = await verifyUser(loginUsername.value, hash)
  if (ok) {
    loginSuccess.value = 'Успешный вход.'
    const user = await getUserByUsername(loginUsername.value)
    if (user) {
      setUser({ id: user.id, username: user.username })
      // expose for debugging
      window.__helpdesk_current_user = user.username
    }
  } else {
    loginError.value = 'Неверные учётные данные.'
  }
}

async function onRegister(e) {
  e.preventDefault()
  regError.value = ''
  regSuccess.value = ''
  if (!regUsername.value || !regPassword.value) {
    regError.value = 'Введите имя пользователя и пароль.'
    return
  }
  try {
    const hash = await hashPassword(regPassword.value)
    await createUser(regUsername.value, hash)
    regSuccess.value = 'Пользователь зарегистрирован. Перейдите на вкладку входа.'
    regUsername.value = ''
    regPassword.value = ''
    tab.value = 'login'
  } catch (err) {
    regError.value = 'Ошибка регистрации: ' + (err && err.message ? err.message : err)
  }
}
</script>

<template>
  <div class="container py-5 auth-root">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card shadow-sm">
          <div class="card-body">
            <ul class="nav nav-tabs mb-3">
              <li class="nav-item">
                <a :class="['nav-link', {active: tab === 'login'}]" href="#" @click.prevent="tab = 'login'">Вход</a>
              </li>
              <li class="nav-item">
                <a :class="['nav-link', {active: tab === 'register'}]" href="#" @click.prevent="tab = 'register'">Регистрация</a>
              </li>
            </ul>

            <div v-if="tab === 'login'">
              <form @submit="onLogin">
                <div class="mb-3">
                  <label class="form-label" for="login-username">Имя пользователя</label>
                  <input id="login-username" v-model="loginUsername" class="form-control" placeholder="например, user@example.com" />
                </div>
                <div class="mb-3">
                  <label class="form-label" for="login-password">Пароль</label>
                  <input id="login-password" v-model="loginPassword" type="password" class="form-control" placeholder="Введите пароль" />
                </div>
                <div class="d-flex justify-content-between align-items-center">
                  <button class="btn btn-primary" type="submit">Войти</button>
                </div>
                <div class="mt-3">
                  <div v-if="loginError" class="text-danger">{{ loginError }}</div>
                  <div v-if="loginSuccess" class="text-success">{{ loginSuccess }}</div>
                </div>
              </form>
            </div>

            <div v-if="tab === 'register'">
              <form @submit="onRegister">
                <div class="mb-3">
                  <label class="form-label" for="reg-username">Имя пользователя</label>
                  <input id="reg-username" v-model="regUsername" class="form-control" placeholder="например, user@example.com" />
                </div>
                <div class="mb-3">
                  <label class="form-label" for="reg-password">Пароль</label>
                  <input id="reg-password" v-model="regPassword" type="password" class="form-control" placeholder="Минимум 6 символов" />
                </div>
                <div class="d-flex justify-content-between align-items-center">
                  <button class="btn btn-secondary" type="submit">Зарегистрироваться</button>
                </div>
                <div class="mt-3">
                  <div v-if="regError" class="text-danger">{{ regError }}</div>
                  <div v-if="regSuccess" class="text-success">{{ regSuccess }}</div>
                </div>
              </form>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Center auth card across the page when layout uses two columns */
.auth-root {
  /* default spacing for small screens — Bootstrap's container handles centering */
}

@media (min-width: 1024px) {
  /* The global layout makes #app a two-column grid on wide screens.
     Make the auth root span both columns and center its contents. */
  .auth-root {
    grid-column: 1 / -1;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: calc(100vh - 4rem);
  }

  .auth-root .card {
    width: 380px; /* consistent card width */
  }
}

/* Small visual tweaks */
.card .card-body { padding: 1.25rem; }
.nav-tabs .nav-link { cursor: pointer; }

</style>
