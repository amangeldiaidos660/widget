<template>
  <NuxtLayout>
    <div class="p-8">
      <div class="max-w-6xl mx-auto">
        <!-- Loading State -->
        <div v-if="loading" class="flex items-center justify-center py-12">
          <div class="text-center">
            <svg class="animate-spin h-12 w-12 text-blue-600 mx-auto mb-4" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <p class="text-gray-600">Loading incident details...</p>
          </div>
        </div>

        <!-- Error State -->
        <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-xl p-6">
          <div class="flex items-center gap-3">
            <svg class="h-6 w-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <div class="text-red-900 font-semibold">{{ error }}</div>
          </div>
        </div>

        <!-- Ticket Content -->
        <div v-else>
          <!-- Header -->
          <div class="mb-6 flex items-center justify-between">
            <div>
              <div class="flex items-center gap-3 mb-2">
                <NuxtLink to="/" class="text-gray-500 hover:text-gray-700">
                  <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                  </svg>
                </NuxtLink>
                <h1 class="text-3xl font-bold text-gray-900">Incident #{{ ticket.id }}</h1>
                <span :class="[
                  'badge',
                  ticket.status === 'NEW' ? 'badge-new' :
                  ticket.status === 'IN_PROGRESS' ? 'badge-in-progress' : 'badge-closed'
                ]">
                  <span class="h-1.5 w-1.5 rounded-full" :class="[
                    ticket.status === 'NEW' ? 'bg-blue-600' :
                    ticket.status === 'IN_PROGRESS' ? 'bg-amber-600' : 'bg-green-600'
                  ]"></span>
                  {{ getStatusLabel(ticket.status) }}
                </span>
              </div>
              <p class="text-gray-600">{{ ticket.project_name }}</p>
            </div>
            <div class="text-right text-sm text-gray-500">
              <div>Created: {{ formatDate(ticket.created_at) }}</div>
              <div>Updated: {{ formatDate(ticket.updated_at) }}</div>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <!-- Main Content -->
            <div class="lg:col-span-2 space-y-6">
              <!-- Reporter Information -->
              <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-6">
                <h2 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                  <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                  Reporter Information
                </h2>
                <div class="grid grid-cols-2 gap-4">
                  <div v-if="ticket.author_name">
                    <div class="text-sm font-semibold text-gray-500 mb-1">Name</div>
                    <div class="text-gray-900">{{ ticket.author_name }}</div>
                  </div>
                  <div v-if="ticket.author_email">
                    <div class="text-sm font-semibold text-gray-500 mb-1">Email</div>
                    <div class="text-gray-900">{{ ticket.author_email }}</div>
                  </div>
                  <div v-if="ticket.author_login">
                    <div class="text-sm font-semibold text-gray-500 mb-1">Login</div>
                    <div class="text-gray-900">{{ ticket.author_login }}</div>
                  </div>
                </div>
              </div>

              <!-- Incident Details -->
              <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-6">
                <h2 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                  <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  Incident Description
                </h2>
                <div class="bg-gray-50 rounded-lg p-4 border border-gray-200">
                  <pre class="text-sm text-gray-900 whitespace-pre-wrap font-sans">{{ ticket.description || 'No description provided' }}</pre>
                </div>
              </div>

              <!-- Diagnostics -->
              <div v-if="hasAnyLogs" class="bg-white rounded-xl border border-gray-200 shadow-sm p-6">
                <h2 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                  <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  Technical Diagnostics
                </h2>
                <div class="space-y-3">
                  <!-- Console Logs -->
                  <details v-if="consoleLogsArr.length" class="group">
                    <summary class="cursor-pointer list-none">
                      <div class="flex items-center justify-between p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                        <div class="flex items-center gap-3">
                          <svg class="h-5 w-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                          </svg>
                          <span class="font-semibold text-blue-900">Console Logs</span>
                          <span class="badge badge-new">{{ consoleLogsArr.length }}</span>
                        </div>
                        <svg class="h-5 w-5 text-blue-600 group-open:rotate-90 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                        </svg>
                      </div>
                    </summary>
                    <div class="mt-2 space-y-2 pl-4">
                      <div v-for="(log, idx) in consoleLogsArr" :key="idx" class="bg-slate-900 rounded-lg p-3">
                        <pre class="text-xs text-green-400 font-mono overflow-x-auto">{{ prettyJson(log) }}</pre>
                      </div>
                    </div>
                  </details>

                  <!-- Network Errors -->
                  <details v-if="networkErrorsArr.length" class="group">
                    <summary class="cursor-pointer list-none">
                      <div class="flex items-center justify-between p-4 bg-red-50 rounded-lg hover:bg-red-100 transition-colors">
                        <div class="flex items-center gap-3">
                          <svg class="h-5 w-5 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                          </svg>
                          <span class="font-semibold text-red-900">Network Errors</span>
                          <span class="badge bg-red-100 text-red-800">{{ networkErrorsArr.length }}</span>
                        </div>
                        <svg class="h-5 w-5 text-red-600 group-open:rotate-90 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                        </svg>
                      </div>
                    </summary>
                    <div class="mt-2 space-y-2 pl-4">
                      <div v-for="(err, idx) in networkErrorsArr" :key="idx" class="bg-slate-900 rounded-lg p-3">
                        <pre class="text-xs text-red-400 font-mono overflow-x-auto">{{ prettyJson(err) }}</pre>
                      </div>
                    </div>
                  </details>

                  <!-- JS Errors -->
                  <details v-if="jsErrorsArr.length" class="group">
                    <summary class="cursor-pointer list-none">
                      <div class="flex items-center justify-between p-4 bg-amber-50 rounded-lg hover:bg-amber-100 transition-colors">
                        <div class="flex items-center gap-3">
                          <svg class="h-5 w-5 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                          </svg>
                          <span class="font-semibold text-amber-900">JavaScript Errors</span>
                          <span class="badge badge-in-progress">{{ jsErrorsArr.length }}</span>
                        </div>
                        <svg class="h-5 w-5 text-amber-600 group-open:rotate-90 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                        </svg>
                      </div>
                    </summary>
                    <div class="mt-2 space-y-2 pl-4">
                      <div v-for="(err, idx) in jsErrorsArr" :key="idx" class="bg-slate-900 rounded-lg p-3">
                        <pre class="text-xs text-amber-400 font-mono overflow-x-auto">{{ prettyJson(err) }}</pre>
                      </div>
                    </div>
                  </details>
                </div>
              </div>
            </div>

            <!-- Sidebar -->
            <div class="lg:col-span-1 space-y-6">
              <!-- Actions -->
              <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-6">
                <h2 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                  <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                  Manage Incident
                </h2>

                <form @submit.prevent="updateTicketHandler" class="space-y-4">
                  <div>
                    <label class="block text-sm font-semibold text-gray-700 mb-2">Status</label>
                    <select v-model="status" class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                      <option value="NEW">New</option>
                      <option value="IN_PROGRESS">In Progress</option>
                      <option value="CLOSED">Resolved</option>
                    </select>
                  </div>

                  <div>
                    <label class="block text-sm font-semibold text-gray-700 mb-2">Assignee</label>
                    <select v-model="assignedTo" class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                      <option value="">Unassigned</option>
                      <option v-for="user in staffUsers" :key="user.id" :value="user.id">
                        {{ user.username }}
                      </option>
                    </select>
                  </div>

                  <button 
                    type="submit"
                    class="w-full bg-blue-600 text-white font-semibold py-2.5 rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                    :disabled="updating"
                  >
                    {{ updating ? 'Saving...' : 'Save Changes' }}
                  </button>

                  <div v-if="updateError" class="bg-red-50 border border-red-200 rounded-lg p-3 text-sm text-red-800">
                    {{ updateError }}
                  </div>
                  <div v-if="updateSuccess" class="bg-green-50 border border-green-200 rounded-lg p-3 text-sm text-green-800">
                    Changes saved successfully!
                  </div>
                </form>
              </div>

              <!-- Metadata -->
              <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-6">
                <h2 class="text-lg font-bold text-gray-900 mb-4">Metadata</h2>
                <div class="space-y-3 text-sm">
                  <div v-if="ticket.page_url">
                    <div class="font-semibold text-gray-500 mb-1">Page URL</div>
                    <a :href="ticket.page_url" target="_blank" class="text-blue-600 hover:underline break-all">
                      {{ ticket.page_url }}
                    </a>
                  </div>
                  <div v-if="ticket.user_agent">
                    <div class="font-semibold text-gray-500 mb-1">User Agent</div>
                    <div class="text-gray-700 text-xs break-all">{{ ticket.user_agent }}</div>
                  </div>
                  <div v-if="ticket.screen_resolution">
                    <div class="font-semibold text-gray-500 mb-1">Screen Resolution</div>
                    <div class="text-gray-700">{{ ticket.screen_resolution }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </NuxtLayout>
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
      error.value = e.message || 'Error loading incident'
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
      updateError.value = e.message || 'Error saving changes'
    } finally {
      updating.value = false
    }
  }

  const getStatusLabel = (status: string) => {
    const labels: Record<string, string> = {
      'NEW': 'New',
      'IN_PROGRESS': 'In Progress',
      'CLOSED': 'Resolved'
    }
    return labels[status] || status
  }

  const formatDate = (dateString: string) => {
    if (!dateString) return 'N/A'
    const date = new Date(dateString)
    return new Intl.DateTimeFormat('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    }).format(date)
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
