
<template>
  <div class="container mt-5">
    <div v-if="loading" class="text-center my-5">
      <span class="spinner-border" role="status"></span>
    </div>
    <div v-else-if="error" class="alert alert-danger">{{ error }}</div>
    <div v-else>
      <h2 class="mb-4">Заявка #{{ ticket.id }}</h2>

      <!-- Категория: Данные заявителя -->
      <div class="mb-4 p-3 border rounded bg-light">
        <h5 class="mb-3">Данные заявителя</h5>
        <table class="table table-sm mb-0">
          <tbody>
            <tr v-if="ticket.author_name">
              <th>Имя</th>
              <td>{{ ticket.author_name }}</td>
            </tr>
            <tr v-if="ticket.author_email">
              <th>Email</th>
              <td>{{ ticket.author_email }}</td>
            </tr>
            <tr v-if="ticket.author_login">
              <th>Логин</th>
              <td>{{ ticket.author_login }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Категория: Данные запроса -->
      <div class="mb-4 p-3 border rounded">
        <h5 class="mb-3">Данные запроса</h5>
        <table class="table table-sm mb-0">
          <tbody>
            <tr v-if="ticket.title">
              <th>Тема</th>
              <td>{{ ticket.title }}</td>
            </tr>
            <tr v-if="ticket.description">
              <th>Описание</th>
              <td><pre class="mb-0">{{ ticket.description }}</pre></td>
            </tr>
            <tr v-if="ticket.created_at">
              <th>Создано</th>
              <td>{{ ticket.created_at }}</td>
            </tr>
            <tr v-if="ticket.updated_at">
              <th>Обновлено</th>
              <td>{{ ticket.updated_at }}</td>
            </tr>
            <tr v-if="ticket.project_name">
              <th>Проект</th>
              <td>{{ ticket.project_name }}</td>
            </tr>
            <tr v-if="ticket.extra">
              <th>Дополнительно</th>
              <td><pre class="mb-0">{{ prettyJson(ticket.extra) }}</pre></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Категория: Диагностика и ошибки -->
      <div v-if="hasAnyLogs" class="mb-4 p-3 border rounded bg-light">
        <h5 class="mb-3">Диагностика и ошибки</h5>
        <div class="accordion" id="logsAccordion">
          <div v-if="consoleLogsArr.length" class="accordion-item">
            <h2 class="accordion-header" id="headingConsole">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseConsole" aria-expanded="false" aria-controls="collapseConsole">
                Console logs ({{ consoleLogsArr.length }})
              </button>
            </h2>
            <div id="collapseConsole" class="accordion-collapse collapse" aria-labelledby="headingConsole" data-bs-parent="#logsAccordion">
              <div class="accordion-body">
                <ul class="list-group">
                  <li v-for="(log, idx) in consoleLogsArr" :key="idx" class="list-group-item">
                    <pre class="mb-0">{{ prettyJson(log) }}</pre>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div v-if="networkErrorsArr.length" class="accordion-item">
            <h2 class="accordion-header" id="headingNetwork">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseNetwork" aria-expanded="false" aria-controls="collapseNetwork">
                Network errors ({{ networkErrorsArr.length }})
              </button>
            </h2>
            <div id="collapseNetwork" class="accordion-collapse collapse" aria-labelledby="headingNetwork" data-bs-parent="#logsAccordion">
              <div class="accordion-body">
                <ul class="list-group">
                  <li v-for="(err, idx) in networkErrorsArr" :key="idx" class="list-group-item">
                    <pre class="mb-0">{{ prettyJson(err) }}</pre>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div v-if="jsErrorsArr.length" class="accordion-item">
            <h2 class="accordion-header" id="headingJs">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseJs" aria-expanded="false" aria-controls="collapseJs">
                JS errors ({{ jsErrorsArr.length }})
              </button>
            </h2>
            <div id="collapseJs" class="accordion-collapse collapse" aria-labelledby="headingJs" data-bs-parent="#logsAccordion">
              <div class="accordion-body">
                <ul class="list-group">
                  <li v-for="(err, idx) in jsErrorsArr" :key="idx" class="list-group-item">
                    <pre class="mb-0">{{ prettyJson(err) }}</pre>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Категория: Действия -->
      <div class="mb-4 p-3 border rounded">
        <h5 class="mb-3">Действия</h5>
        <form @submit.prevent="updateTicketHandler">
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
  </div>
</template>
<script setup lang="ts">
  import { ref, onMounted, computed } from 'vue'
  import { useRoute } from 'vue-router'
  import { getTicket, updateTicket } from '~/api/tickets'
  import { getStaffUsers } from '~/api/users'
  import { useAuthStore } from '~/stores/auth'

  const route = useRoute()
  const ticket = ref({})
  const loading = ref(true)
  const error = ref('')
  const status = ref('')
  const assignedTo = ref('')
  const updating = ref(false)
  const updateError = ref('')
  const updateSuccess = ref(false)
  const staffUsers = ref([])
  const authStore = useAuthStore()

  const consoleLogsArr = computed(() => {
    try { return ticket.value.console_logs ? JSON.parse(ticket.value.console_logs) : [] }
    catch { return [] }
  })
  const networkErrorsArr = computed(() => {
    try { return ticket.value.network_errors ? JSON.parse(ticket.value.network_errors) : [] }
    catch { return [] }
  })
  const jsErrorsArr = computed(() => {
    try { return ticket.value.js_errors ? JSON.parse(ticket.value.js_errors) : [] }
    catch { return [] }
  })
  const hasAnyLogs = computed(() =>
    consoleLogsArr.value.length ||
    networkErrorsArr.value.length ||
    jsErrorsArr.value.length
  )

  const fetchStaffUsers = async () => {
    try {
      staffUsers.value = await getStaffUsers(authStore.token)
    } catch {
      staffUsers.value = []
    }
  }

  const fetchTicket = async () => {
    loading.value = true
    error.value = ''
    try {
      const data = await getTicket(route.query.id, authStore.token)
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
      await updateTicket(ticket.value.id, {
        status: status.value,
        assigned_to: assignedTo.value
      }, authStore.token)
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

  const prettyJson = (val: any) => {
    if (typeof val === 'string') {
      try { return JSON.stringify(JSON.parse(val), null, 2) }
      catch { return val }
    }
    return JSON.stringify(val, null, 2)
  }
</script>