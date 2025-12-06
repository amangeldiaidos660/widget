<template>
  <NuxtLayout>
    <div class="p-8">
      <!-- Header -->
      <div class="mb-6">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">{{ t.dashboard.title }}</h1>
        <p class="text-gray-600">{{ t.dashboard.subtitle }}</p>
      </div>

      <!-- Stats -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
        <div class="rounded-lg bg-white p-6 shadow">
          <p class="text-sm font-medium text-gray-600">{{ t.dashboard.totalIncidents }}</p>
          <p class="mt-2 text-3xl font-bold text-gray-900">{{ tickets.length }}</p>
        </div>
        <div class="rounded-lg bg-white p-6 shadow">
          <p class="text-sm font-medium text-gray-600">{{ t.dashboard.new }}</p>
          <p class="mt-2 text-3xl font-bold text-blue-600">{{ newCount }}</p>
        </div>
        <div class="rounded-lg bg-white p-6 shadow">
          <p class="text-sm font-medium text-gray-600">{{ t.dashboard.inProgress }}</p>
          <p class="mt-2 text-3xl font-bold text-amber-600">{{ inProgressCount }}</p>
        </div>
        <div class="rounded-lg bg-white p-6 shadow">
          <p class="text-sm font-medium text-gray-600">{{ t.dashboard.resolved }}</p>
          <p class="mt-2 text-3xl font-bold text-green-600">{{ closedCount }}</p>
        </div>
      </div>

      <!-- Table -->
      <div class="overflow-hidden rounded-lg bg-white shadow">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">ID</th>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">{{ t.dashboard.description }}</th>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">{{ t.dashboard.reporter }}</th>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">{{ t.dashboard.assignedTo }}</th>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">{{ t.dashboard.status }}</th>
              <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">{{ t.dashboard.created }}</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200 bg-white">
            <tr v-if="loading" v-for="i in 5" :key="i" class="animate-pulse">
              <td colspan="6" class="px-6 py-4">
                <div class="h-4 bg-gray-200 rounded w-full"></div>
              </td>
            </tr>
            <tr v-else-if="tickets.length === 0">
              <td colspan="6" class="px-6 py-8 text-center text-sm text-gray-500">
                {{ t.dashboard.noIncidents }}
              </td>
            </tr>
            <tr v-else v-for="ticket in tickets" :key="ticket.id" class="hover:bg-gray-50 transition-colors cursor-pointer" @click="goToTicket(ticket.id)">
              <td class="whitespace-nowrap px-6 py-4 text-sm font-medium text-blue-600">
                {{ ticket.ticket_id }}
              </td>
              <td class="px-6 py-4">
                <div class="text-sm font-medium text-gray-900 max-w-md truncate">{{ getTitle(ticket.description) }}</div>
                <div class="text-sm text-gray-500">{{ ticket.project_name }}</div>
              </td>
              <td class="whitespace-nowrap px-6 py-4">
                <div class="text-sm text-gray-900">{{ ticket.author_name || t.dashboard.anonymous }}</div>
                <div class="text-sm text-gray-500">{{ ticket.author_email || 'N/A' }}</div>
              </td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">
                {{ ticket.assigned_to_username || t.dashboard.unassigned }}
              </td>
              <td class="whitespace-nowrap px-6 py-4">
                <span :class="getStatusClass(ticket.status)" class="inline-flex rounded-full px-2 py-1 text-xs font-semibold">
                  {{ getStatusLabel(ticket.status) }}
                </span>
              </td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-500">
                {{ formatDate(ticket.created_at) }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useLanguageStore } from '~/stores/language'
import { useAuthStore } from '~/stores/auth'
import { useRouter } from 'vue-router'
import { getTickets } from '~/api/tickets'

const langStore = useLanguageStore()
const authStore = useAuthStore()
const t = computed(() => langStore.t)
const router = useRouter()

const tickets = ref([])
const loading = ref(true)

const newCount = computed(() => tickets.value.filter(t => t.status === 'NEW').length)
const inProgressCount = computed(() => tickets.value.filter(t => t.status === 'IN_PROGRESS').length)
const closedCount = computed(() => tickets.value.filter(t => t.status === 'CLOSED').length)

const getTitle = (description) => {
  return description?.split('\n')[0] || description
}

const getStatusClass = (status) => {
  const classes = {
    NEW: 'bg-blue-100 text-blue-800',
    IN_PROGRESS: 'bg-amber-100 text-amber-800',
    CLOSED: 'bg-green-100 text-green-800'
  }
  return classes[status] || 'bg-gray-100 text-gray-800'
}

const getStatusLabel = (status) => {
  const labels = {
    NEW: t.value.dashboard.new,
    IN_PROGRESS: t.value.dashboard.inProgress,
    CLOSED: t.value.dashboard.resolved
  }
  return labels[status] || status
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('ru-RU', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const goToTicket = (id) => {
  router.push(`/TicketDetail?id=${id}`)
}

const fetchTickets = async () => {
  try {
    loading.value = true
    const data = await getTickets({}, authStore.token)
    tickets.value = data.results || []
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
</script>
