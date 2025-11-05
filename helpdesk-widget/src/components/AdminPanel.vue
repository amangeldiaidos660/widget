<script setup>
import { ref, onMounted } from 'vue'
import state, { setUser, clearUser } from '../stores/auth'
import { createComponent, getComponentsByUser } from '../services/db'
import { getUserByUsername } from '../services/db'

const components = ref([])
const name = ref('')
const message = ref('')

async function load() {
  if (!state.user) return
  components.value = await getComponentsByUser(state.user.id)
}

onMounted(load)

async function onCreate(e) {
  e.preventDefault()
  message.value = ''
  if (!name.value) {
    message.value = 'Введите имя компонента.'
    return
  }
  try {
    const res = await createComponent(state.user.id, name.value)
    name.value = ''
    message.value = 'Компонент создан.'
    await load()
  } catch (err) {
    message.value = 'Ошибка: ' + (err.message || err)
  }
}

function onLogout() {
  clearUser()
}

function copyCode(code) {
  navigator.clipboard.writeText(code)
}
</script>

<template>
  <div class="container py-4 admin-root">
    <div class="admin-inner">
      <div class="header d-flex justify-content-between align-items-center mb-3">
        <div>
          <h4 class="mb-0">Админ-панель</h4>
          <small class="text-muted">Управление виджетами</small>
        </div>
        <div class="d-flex align-items-center">
          <span class="me-3">{{ state.user?.username }}</span>
          <button class="btn btn-sm btn-outline-secondary" @click="onLogout">Выйти</button>
        </div>
      </div>

      <!-- Create form -->
      <div class="card mb-3">
        <div class="card-body">
          <form @submit="onCreate" class="row g-2 align-items-center">
            <div class="col-12 col-md-9">
              <label class="form-label" for="component-name">Название виджета</label>
              <input id="component-name" v-model="name" class="form-control w-100" placeholder="Название виджета" />
            </div>
            <div class="col-12 col-md-3 d-grid">
              <label class="form-label d-none d-md-block">&nbsp;</label>
              <button class="btn btn-primary w-100">Создать компонент</button>
            </div>
          </form>
          <div class="mt-2 text-success" v-if="message">{{ message }}</div>
        </div>
      </div>

      <!-- Components list -->
      <div class="card">
        <div class="card-body">
          <h5>Список компонентов</h5>
          <div class="table-responsive">
            <table class="table table-sm mt-2 mb-0">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Название</th>
                  <th>Код вставки</th>
                  <th>Дата</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="c in components" :key="c.id">
                  <td>{{ c.id }}</td>
                  <td>{{ c.name }}</td>
                  <td><code style="white-space: pre-wrap">{{ c.script_code }}</code></td>
                  <td>{{ c.created_at }}</td>
                  <td><button class="btn btn-sm btn-outline-secondary" @click.prevent="copyCode(c.script_code)">Копировать</button></td>
                </tr>
                <tr v-if="!components.length"><td colspan="5" class="text-muted">Нет компонентов</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.admin-root {
  display:flex;
  align-items:center;
  justify-content:center;
  min-height: calc(100vh - 4rem);
}

.admin-inner { max-width: 920px; margin: 0 auto; width: 100%; }
.admin-root .header h4 { font-weight: 600; }
</style>
