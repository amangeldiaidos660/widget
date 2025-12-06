<template>
  <NuxtLayout>
    <div class="p-8">
      <!-- Header -->
      <div class="mb-6">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">{{ t.tickets.title }}</h1>
        <p class="text-gray-600">{{ t.tickets.subtitle }}</p>
      </div>

      <!-- Actions and Filters -->
      <div class="mb-6 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <select v-model="filters.status" @change="fetchTickets" class="rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500">
            <option value="">{{ t.tickets.filterByStatus }}</option>
            <option value="NEW">{{ t.dashboard.new }}</option>
            <option value="IN_PROGRESS">{{ t.dashboard.inProgress }}</option>
            <option value="CLOSED">{{ t.dashboard.resolved }}</option>
          </select>
          
          <select v-model="filters.priority" class="rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500">
            <option value="">{{ t.tickets.filterByPriority }}</option>
            <option value="high">{{ t.tickets.high }}</option>
            <option value="medium">{{ t.tickets.medium }}</option>
            <option value="low">{{ t.tickets.low }}</option>
          </select>

          <input 
            v-model="filters.search"
            @input="onSearchInput"
            type="text" 
            :placeholder="t.common.search" 
            class="rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500 w-64" />
        </div>

        <button class="flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2 text-sm font-semibold text-white hover:bg-blue-700 transition-colors">
          <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          {{ t.tickets.createNew }}
        </button>
      </div>

      <!-- Tickets Table -->
      <div class="overflow-hidden rounded-lg bg-white shadow">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">ID</th>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">{{ t.dashboard.description }}</th>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">{{ t.tickets.priority }}</th>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">{{ t.dashboard.status }}</th>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">{{ t.tickets.assignee }}</th>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">{{ t.tickets.dueDate }}</th>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500"></th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200 bg-white">
            <tr v-for="ticket in filteredTickets" :key="ticket.id" class="hover:bg-gray-50 transition-colors">
              <td class="whitespace-nowrap px-6 py-4 text-sm font-medium text-gray-900">
                #{{ ticket.id }}
              </td>
              <td class="px-6 py-4">
                <div class="text-sm font-medium text-gray-900">{{ ticket.title }}</div>
                <div class="text-sm text-gray-500">{{ ticket.description }}</div>
              </td>
              <td class="whitespace-nowrap px-6 py-4">
                <span :class="getPriorityClass(ticket.priority)" class="inline-flex rounded-full px-2 py-1 text-xs font-semibold">
                  {{ getPriorityLabel(ticket.priority) }}
                </span>
              </td>
              <td class="whitespace-nowrap px-6 py-4">
                <span :class="getStatusClass(ticket.status)" class="inline-flex rounded-full px-2 py-1 text-xs font-semibold">
                  {{ getStatusLabel(ticket.status) }}
                </span>
              </td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">
                {{ ticket.assignee || t.dashboard.unassigned }}
              </td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-500">
                {{ formatDate(ticket.dueDate) }}
              </td>
              <td class="whitespace-nowrap px-6 py-4 text-right text-sm font-medium">
                <NuxtLink :to="`/TicketDetail?id=${ticket.id}`" class="text-blue-600 hover:text-blue-900">
                  {{ t.tickets.viewDetails }}
                </NuxtLink>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Empty State -->
        <div v-if="filteredTickets.length === 0" class="py-12 text-center">
          <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <h3 class="mt-2 text-sm font-medium text-gray-900">{{ t.dashboard.noIncidents }}</h3>
          <p class="mt-1 text-sm text-gray-500">{{ t.tickets.createNew }}</p>
        </div>
      </div>

      <!-- Pagination -->
      <div class="mt-6 flex items-center justify-between">
        <div class="text-sm text-gray-700">
          {{ t.common.page }} {{ currentPage }} {{ t.common.of }} {{ totalPages }} ({{ t.common.total }}: {{ filteredTickets.length }})
        </div>
        <div class="flex gap-2">
          <button 
            @click="currentPage--" 
            :disabled="currentPage === 1"
            class="rounded-lg border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {{ t.common.previous }}
          </button>
          <button 
            @click="currentPage++" 
            :disabled="currentPage === totalPages"
            class="rounded-lg border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {{ t.common.next }}
          </button>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useLanguageStore } from '~/stores/language'
import { useAuthStore } from '~/stores/auth'
import { getTickets } from '~/api/tickets'

const langStore = useLanguageStore()
const authStore = useAuthStore()
const t = computed(() => langStore.t)

const filters = ref({
  status: '',
  priority: '',
  search: ''
})

const loading = ref(true)
const currentPage = ref(1)
const totalPages = ref(1)
const totalCount = ref(0)

const tickets = ref([])
let searchTimeout = null

const onSearchInput = () => {
  if (searchTimeout) {
    clearTimeout(searchTimeout)
  }
  searchTimeout = setTimeout(() => {
    currentPage.value = 1
    fetchTickets()
  }, 500)
}

const fetchTickets = async () => {
  loading.value = true
  try {
    const params = {
      page: currentPage.value
    }
    if (filters.value.status) {
      params.status = filters.value.status.toUpperCase()
    }
    if (filters.value.search) {
      params.search = filters.value.search
    }
    
    const data = await getTickets(params, authStore.token)
    tickets.value = data.results.map(ticket => ({
      id: ticket.id,
      ticket_id: ticket.ticket_id,
      title: ticket.description?.split('\n')[0] || ticket.description,
      description: ticket.description,
      priority: 'medium',
      status: ticket.status.toLowerCase().replace('_', ' '),
      assignee: ticket.assigned_to_username,
      dueDate: ticket.created_at,
      created_at: ticket.created_at
    }))
    totalCount.value = data.count
    totalPages.value = Math.ceil(data.count / 50)
  } catch (error) {
    console.error('Error fetching tickets:', error)
    tickets.value = []
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchTickets()
})

const changePage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page
    fetchTickets()
  }
}

const filteredTickets = computed(() => {
  let result = tickets.value
  
  // Локальная фильтрация по приоритету (т.к. его нет в API)
  if (filters.value.priority) {
    result = result.filter(ticket => ticket.priority === filters.value.priority)
  }
  
  return result
})

const getPriorityClass = (priority) => {
  const classes = {
    high: 'bg-red-100 text-red-800',
    medium: 'bg-amber-100 text-amber-800',
    low: 'bg-green-100 text-green-800'
  }
  return classes[priority] || 'bg-gray-100 text-gray-800'
}

const getPriorityLabel = (priority) => {
  const labels = {
    high: t.value.tickets.high,
    medium: t.value.tickets.medium,
    low: t.value.tickets.low
  }
  return labels[priority] || priority
}

const getStatusClass = (status) => {
  const classes = {
    new: 'bg-blue-100 text-blue-800',
    'in progress': 'bg-amber-100 text-amber-800',
    resolved: 'bg-green-100 text-green-800',
    closed: 'bg-green-100 text-green-800'
  }
  return classes[status] || 'bg-gray-100 text-gray-800'
}

const getStatusLabel = (status) => {
  const labels = {
    new: t.value.dashboard.new,
    'in progress': t.value.dashboard.inProgress,
    'in_progress': t.value.dashboard.inProgress,
    resolved: t.value.dashboard.resolved,
    closed: t.value.dashboard.resolved
  }
  return labels[status] || status
}

const formatDate = (date) => {
  if (!date) return 'N/A'
  return new Date(date).toLocaleDateString('ru-RU')
}
</script>
