<template>
  <NuxtLayout>
    <div class="p-8">
      <!-- Header -->
      <div class="mb-6">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">{{ t.reports.title }}</h1>
        <p class="text-gray-600">{{ t.reports.subtitle }}</p>
      </div>

      <!-- Actions -->
      <div class="mb-6 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <input 
            v-model="dateRange.start" 
            type="date" 
            class="rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500" />
          <span class="text-gray-500">—</span>
          <input 
            v-model="dateRange.end" 
            type="date" 
            class="rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500" />
          <button class="rounded-lg bg-blue-600 px-4 py-2 text-sm font-semibold text-white hover:bg-blue-700 transition-colors">
            {{ t.reports.generateReport }}
          </button>
        </div>

        <div class="flex gap-2">
          <button class="flex items-center gap-2 rounded-lg border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors">
            <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M9 19l3 3m0 0l3-3m-3 3V10" />
            </svg>
            {{ t.reports.exportPdf }}
          </button>
          <button class="flex items-center gap-2 rounded-lg border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors">
            <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            {{ t.reports.exportExcel }}
          </button>
        </div>
      </div>

      <!-- Stats Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div class="rounded-lg bg-white p-6 shadow">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">{{ t.dashboard.totalIncidents }}</p>
              <p class="mt-2 text-3xl font-bold text-gray-900">{{ stats.total }}</p>
              <p class="mt-1 text-sm text-gray-500">Всего заявок</p>
            </div>
            <div class="rounded-full bg-blue-100 p-3">
              <svg class="h-6 w-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
          </div>
        </div>

        <div class="rounded-lg bg-white p-6 shadow">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">{{ t.dashboard.new }}</p>
              <p class="mt-2 text-3xl font-bold text-gray-900">{{ stats.new }}</p>
              <p class="mt-1 text-sm text-gray-500">Новых заявок</p>
            </div>
            <div class="rounded-full bg-amber-100 p-3">
              <svg class="h-6 w-6 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
        </div>

        <div class="rounded-lg bg-white p-6 shadow">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">{{ t.dashboard.inProgress }}</p>
              <p class="mt-2 text-3xl font-bold text-gray-900">{{ stats.in_progress }}</p>
              <p class="mt-1 text-sm text-gray-500">В работе</p>
            </div>
            <div class="rounded-full bg-green-100 p-3">
              <svg class="h-6 w-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
        </div>

        <div class="rounded-lg bg-white p-6 shadow">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">{{ t.dashboard.resolved }}</p>
              <p class="mt-2 text-3xl font-bold text-gray-900">{{ stats.closed }}</p>
              <p class="mt-1 text-sm text-gray-500">Решенных</p>
            </div>
            <div class="rounded-full bg-purple-100 p-3">
              <svg class="h-6 w-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" />
              </svg>
            </div>
          </div>
        </div>
      </div>

      <!-- Charts Row -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        <!-- Incidents by Status -->
        <div class="rounded-lg bg-white p-6 shadow">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">{{ t.reports.incidentsByStatus }}</h3>
          <div class="space-y-4">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-sm font-medium text-gray-700">{{ t.dashboard.new }}</span>
                <span class="text-sm font-semibold text-gray-900">45 (18%)</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div class="bg-blue-600 h-2 rounded-full" style="width: 18%"></div>
              </div>
            </div>
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-sm font-medium text-gray-700">{{ t.dashboard.inProgress }}</span>
                <span class="text-sm font-semibold text-gray-900">82 (33%)</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div class="bg-amber-600 h-2 rounded-full" style="width: 33%"></div>
              </div>
            </div>
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-sm font-medium text-gray-700">{{ t.dashboard.resolved }}</span>
                <span class="text-sm font-semibold text-gray-900">120 (49%)</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div class="bg-green-600 h-2 rounded-full" style="width: 49%"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Incidents by Priority -->
        <div class="rounded-lg bg-white p-6 shadow">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">{{ t.reports.incidentsByPriority }}</h3>
          <div class="space-y-4">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-sm font-medium text-gray-700">{{ t.tickets.high }}</span>
                <span class="text-sm font-semibold text-gray-900">67 (27%)</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div class="bg-red-600 h-2 rounded-full" style="width: 27%"></div>
              </div>
            </div>
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-sm font-medium text-gray-700">{{ t.tickets.medium }}</span>
                <span class="text-sm font-semibold text-gray-900">118 (48%)</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div class="bg-amber-600 h-2 rounded-full" style="width: 48%"></div>
              </div>
            </div>
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-sm font-medium text-gray-700">{{ t.tickets.low }}</span>
                <span class="text-sm font-semibold text-gray-900">62 (25%)</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div class="bg-green-600 h-2 rounded-full" style="width: 25%"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Top Issues -->
      <div class="rounded-lg bg-white p-6 shadow mb-8">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">{{ t.reports.topIssues }}</h3>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead>
              <tr>
                <th class="px-4 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">{{ t.dashboard.description }}</th>
                <th class="px-4 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">Количество</th>
                <th class="px-4 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">Тренд</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 bg-white">
              <tr>
                <td class="px-4 py-3 text-sm text-gray-900">Проблемы с API Gateway timeout</td>
                <td class="px-4 py-3 text-sm text-gray-900">34</td>
                <td class="px-4 py-3 text-sm text-green-600">↓ 12%</td>
              </tr>
              <tr>
                <td class="px-4 py-3 text-sm text-gray-900">Медленная загрузка дашборда</td>
                <td class="px-4 py-3 text-sm text-gray-900">28</td>
                <td class="px-4 py-3 text-sm text-red-600">↑ 8%</td>
              </tr>
              <tr>
                <td class="px-4 py-3 text-sm text-gray-900">Ошибки валидации форм</td>
                <td class="px-4 py-3 text-sm text-gray-900">21</td>
                <td class="px-4 py-3 text-sm text-green-600">↓ 5%</td>
              </tr>
              <tr>
                <td class="px-4 py-3 text-sm text-gray-900">Проблемы с базой данных</td>
                <td class="px-4 py-3 text-sm text-gray-900">19</td>
                <td class="px-4 py-3 text-sm text-gray-600">→ 0%</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Team Productivity -->
      <div class="rounded-lg bg-white p-6 shadow">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">{{ t.reports.teamProductivity }}</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="rounded-lg border border-gray-200 p-4">
            <div class="flex items-center justify-between mb-2">
              <span class="text-sm font-medium text-gray-700">Б. Нұрлан</span>
              <span class="text-xs text-gray-500">Backend</span>
            </div>
            <p class="text-2xl font-bold text-gray-900">42</p>
            <p class="text-sm text-gray-500">Решено инцидентов</p>
          </div>
          <div class="rounded-lg border border-gray-200 p-4">
            <div class="flex items-center justify-between mb-2">
              <span class="text-sm font-medium text-gray-700">А. Айгуль</span>
              <span class="text-xs text-gray-500">Frontend</span>
            </div>
            <p class="text-2xl font-bold text-gray-900">38</p>
            <p class="text-sm text-gray-500">Решено инцидентов</p>
          </div>
          <div class="rounded-lg border border-gray-200 p-4">
            <div class="flex items-center justify-between mb-2">
              <span class="text-sm font-medium text-gray-700">К. Ержан</span>
              <span class="text-xs text-gray-500">DevOps</span>
            </div>
            <p class="text-2xl font-bold text-gray-900">35</p>
            <p class="text-sm text-gray-500">Решено инцидентов</p>
          </div>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useLanguageStore } from '~/stores/language'
import { useAuthStore } from '~/stores/auth'
import { getTickets } from '~/api/tickets'
import { apiGet } from '~/api/client'
import { API_ENDPOINTS } from '~/api/backendEndpoints'

const langStore = useLanguageStore()
const authStore = useAuthStore()
const t = computed(() => langStore.t)

const dateRange = ref({
  start: '2025-11-01',
  end: '2025-12-07'
})

const loading = ref(true)
const stats = ref({
  total: 0,
  new: 0,
  in_progress: 0,
  closed: 0
})

const tickets = ref([])

const fetchStats = async () => {
  loading.value = true
  try {
    const data = await apiGet(API_ENDPOINTS.health.replace('/health/', '/stats/'), authStore.token)
    stats.value = data
  } catch (error) {
    console.error('Error fetching stats:', error)
  } finally {
    loading.value = false
  }
}

const fetchTickets = async () => {
  try {
    const data = await getTickets({}, authStore.token)
    tickets.value = data.results || []
  } catch (error) {
    console.error('Error fetching tickets:', error)
  }
}

onMounted(() => {
  fetchStats()
  fetchTickets()
})
</script>
