<template>
  <div class="container mt-5">
    <div v-if="loading" class="text-center my-5">
      <span class="spinner-border" role="status"></span>
    </div>
    <div v-else-if="error" class="alert alert-danger">{{ error }}</div>
    <div v-else>
      <h2 class="mb-4">Заявка #{{ ticket.id }}</h2>
      <table class="table table-bordered">
        <tbody>
          <tr v-for="(value, key) in ticket" :key="key" v-if="!['console_logs','network_errors','js_errors'].includes(key)">
            <th>{{ key }}</th>
            <td>
              <pre v-if="typeof value === 'object' && value !== null">{{ value }}</pre>
              <span v-else>{{ value }}</span>
            </td>
          </tr>
          <tr v-if="ticket.console_logs">
            <th>console_logs</th>
            <td><pre style="white-space: pre-wrap; word-break: break-all;">{{ ticket.console_logs }}</pre></td>
          </tr>
          <tr v-if="ticket.network_errors">
            <th>network_errors</th>
            <td><pre style="white-space: pre-wrap; word-break: break-all;">{{ ticket.network_errors }}</pre></td>
          </tr>
          <tr v-if="ticket.js_errors">
            <th>js_errors</th>
            <td><pre style="white-space: pre-wrap; word-break: break-all;">{{ ticket.js_errors }}</pre></td>
          </tr>
        </tbody>
      </table>
      <form @submit.prevent="updateTicketHandler" class="mt-4">
        <div class="mb-3">
          <label class="form-label">Статус</label>
          <select v-model="status" class="form-select">
            <option value="NEW">Новая</option>
            <option value="IN_PROGRESS">В работе</option>
            <option value="CLOSED">Закрыта</option>
          </select>
        </div>
        <div class="mb-3">
          <label class="form-label">Ответственный</label>
          <select v-model="assignedTo" class="form-select">
            <option value="">Не назначен</option>
            <option v-for="user in staffUsers" :key="user.id" :value="user.id">
              {{ user.username }}
            </option>
          </select>
        </div>
        <button class="btn btn-primary" :disabled="updating">Сохранить</button>
      </form>
      <div v-if="updateError" class="alert alert-danger mt-3">{{ updateError }}</div>
      <div v-if="updateSuccess" class="alert alert-success mt-3">Изменения сохранены!</div>
    </div>
  </div>
</template>


<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getTicket, updateTicket } from '~/api/tickets'
import { getStaffUsers } from '~/api/users'
import { useAuthStore } from '~/stores/auth'

const route = useRoute()
const ticket = ref<any>({})
const loading = ref(true)
const error = ref('')
const status = ref('')
const assignedTo = ref('')
const updating = ref(false)
const updateError = ref('')
const updateSuccess = ref(false)
const staffUsers = ref<any[]>([])
const authStore = useAuthStore()

const fetchStaffUsers = async () => {
  try {
    staffUsers.value = await getStaffUsers(authStore.token)
  } catch (e) {
    staffUsers.value = []
  }
}

const fetchTicket = async () => {
  loading.value = true
  error.value = ''
  try {
    const data = await getTicket(route.query.id)
    ticket.value = data
    status.value = data.status
    assignedTo.value = data.assigned_to || ''
  } catch (e: any) {
    error.value = e.message || 'Ошибка загрузки заявки'
  } finally {
    loading.value = false
  }
}

const updateTicketHandler = async () => {
  updating.value = true
  updateError.value = ''
  updateSuccess.value = false
  try {
    await updateTicket(ticket.value.id, { status: status.value, assigned_to: assignedTo.value })
    updateSuccess.value = true
    fetchTicket()
  } catch (e: any) {
    updateError.value = e.message || 'Ошибка сохранения'
  } finally {
    updating.value = false
  }
}

onMounted(() => {
  fetchStaffUsers()
  fetchTicket()
})
</script>
