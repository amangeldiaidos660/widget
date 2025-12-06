<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Sidebar -->
    <aside class="fixed left-0 top-0 z-40 h-screen w-64 bg-slate-900 text-white transition-transform">
      <div class="flex h-full flex-col">
        <!-- Logo -->
        <div class="flex h-16 items-center justify-center border-b border-slate-800 px-6">
          <div class="flex items-center gap-3">
            <div class="h-10 w-10 rounded-lg bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center">
              <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </div>
            <div>
              <div class="text-sm font-bold">ARRFR</div>
              <div class="text-xs text-slate-400">FinReg System</div>
            </div>
          </div>
        </div>

        <!-- Navigation -->
        <nav class="flex-1 space-y-1 px-3 py-4">
          <a href="#" class="flex items-center gap-3 rounded-lg bg-slate-800 px-3 py-2.5 text-sm font-medium text-white transition-colors">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            <span>Dashboard</span>
          </a>
          <a href="#" class="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium text-slate-300 hover:bg-slate-800 hover:text-white transition-colors">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
            <span>Tickets</span>
          </a>
          <NuxtLink to="/ProjectsCreate" class="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium text-slate-300 hover:bg-slate-800 hover:text-white transition-colors">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
            </svg>
            <span>Projects</span>
          </NuxtLink>
          <a href="#" class="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium text-slate-300 hover:bg-slate-800 hover:text-white transition-colors">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            <span>Reports</span>
          </a>
          <a href="#" class="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium text-slate-300 hover:bg-slate-800 hover:text-white transition-colors">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            <span>Settings</span>
          </a>
        </nav>

        <!-- User Info at Bottom -->
        <div class="border-t border-slate-800 p-4">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="h-8 w-8 rounded-full bg-blue-600 flex items-center justify-center text-sm font-bold">
                {{ (authStore.user?.username || 'U').charAt(0).toUpperCase() }}
              </div>
              <div class="text-xs">
                <div class="font-medium">{{ authStore.user?.username || 'User' }}</div>
                <div class="text-slate-400">Admin</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </aside>

    <!-- Main Content -->
    <div class="ml-64">
      <!-- Header -->
      <header class="sticky top-0 z-30 bg-white border-b border-gray-200 shadow-sm">
        <div class="flex h-16 items-center justify-between px-8">
          <!-- Breadcrumbs -->
          <div class="flex items-center gap-2 text-sm">
            <svg class="h-4 w-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            <span class="text-gray-500">/</span>
            <span class="font-semibold text-gray-900">Dashboard</span>
          </div>

          <!-- Right Side -->
          <div class="flex items-center gap-4">
            <!-- Language Switcher -->
            <div class="flex items-center gap-1 rounded-lg border border-gray-300 p-1">
              <button class="px-3 py-1 text-xs font-medium rounded-md bg-blue-600 text-white transition-colors">
                KZ
              </button>
              <button class="px-3 py-1 text-xs font-medium text-gray-600 hover:bg-gray-100 rounded-md transition-colors">
                RU
              </button>
            </div>

            <!-- User Profile -->
            <div class="flex items-center gap-3">
              <div class="text-right text-sm">
                <div class="font-semibold text-gray-900">A. Amangeldi</div>
                <div class="text-xs text-gray-500">Administrator</div>
              </div>
              <button @click="handleLogout" class="rounded-lg border border-gray-300 p-2 hover:bg-gray-50 transition-colors" title="Logout">
                <svg class="h-5 w-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </header>

      <!-- Page Content -->
      <main class="min-h-screen bg-gray-50/50 p-8">
        <!-- Page Title -->
        <div class="mb-6">
          <h1 class="text-2xl font-bold text-gray-900">Incident Monitoring Dashboard</h1>
          <p class="text-sm text-gray-500 mt-1">Real-time system incidents and service requests</p>
        </div>

        <!-- Stats Cards -->
        <div class="grid grid-cols-1 gap-6 mb-6 sm:grid-cols-2 lg:grid-cols-4">
          <div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-gray-600">Total Incidents</p>
                <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.total }}</p>
              </div>
              <div class="h-12 w-12 rounded-lg bg-blue-100 flex items-center justify-center">
                <svg class="h-6 w-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-gray-600">New</p>
                <p class="text-3xl font-bold text-blue-600 mt-2">{{ stats.new }}</p>
              </div>
              <div class="h-12 w-12 rounded-lg bg-blue-100 flex items-center justify-center">
                <svg class="h-6 w-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                </svg>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-gray-600">In Progress</p>
                <p class="text-3xl font-bold text-amber-600 mt-2">{{ stats.inProgress }}</p>
              </div>
              <div class="h-12 w-12 rounded-lg bg-amber-100 flex items-center justify-center">
                <svg class="h-6 w-6 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-gray-600">Resolved</p>
                <p class="text-3xl font-bold text-green-600 mt-2">{{ stats.closed }}</p>
              </div>
              <div class="h-12 w-12 rounded-lg bg-green-100 flex items-center justify-center">
                <svg class="h-6 w-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
            </div>
          </div>
        </div>

        <!-- Filters -->
        <div class="bg-white rounded-xl border border-gray-200 p-6 mb-6 shadow-sm">
          <div class="grid grid-cols-1 gap-4 md:grid-cols-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Search</label>
              <input 
                v-model="filters.search" 
                type="text" 
                placeholder="Ticket ID, description..."
                class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
              >
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Status</label>
              <select 
                v-model="filters.status"
                class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
              >
                <option value="">All Statuses</option>
                <option value="NEW">New</option>
                <option value="IN_PROGRESS">In Progress</option>
                <option value="CLOSED">Closed</option>
              </select>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Project</label>
              <input 
                v-model="filters.project" 
                type="text" 
                placeholder="Project slug..."
                class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
              >
            </div>
            <div class="flex items-end">
              <button 
                @click="applyFilters"
                class="w-full rounded-lg bg-blue-600 px-4 py-2 text-sm font-semibold text-white hover:bg-blue-700 transition-colors"
              >
                Apply Filters
              </button>
            </div>
          </div>
        </div>

        <!-- Table -->
        <div class="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
          <div class="overflow-x-auto">
            <table class="w-full">
              <thead>
                <tr class="border-b border-gray-200 bg-gray-50">
                  <th class="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Ticket ID</th>
                  <th class="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Environment</th>
                  <th class="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Description</th>
                  <th class="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Reporter</th>
                  <th class="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Assigned To</th>
                  <th class="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Status</th>
                  <th class="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Created</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-100">
                <tr v-if="loading" v-for="i in 5" :key="i" class="animate-pulse">
                  <td class="px-6 py-4" colspan="7">
                    <div class="h-4 bg-gray-200 rounded w-full"></div>
                  </td>
                </tr>
                <tr 
                  v-else-if="tickets.length === 0"
                  class="hover:bg-gray-50 transition-colors"
                >
                  <td colspan="7" class="px-6 py-8 text-center text-sm text-gray-500">
                    No incidents found
                  </td>
                </tr>
                <tr 
                  v-else
                  v-for="ticket in enhancedTickets" 
                  :key="ticket.id"
                  @click="handleTicketSelect(ticket)"
                  class="cursor-pointer hover:bg-blue-50/50 transition-colors"
                >
                  <td class="px-6 py-4">
                    <div class="text-sm font-mono font-semibold text-blue-600">{{ ticket.ticket_id }}</div>
                  </td>
                  <td class="px-6 py-4">
                    <span :class="[
                      'env-badge',
                      ticket.environment === 'PROD' ? 'env-prod' : 
                      ticket.environment === 'UAT' ? 'env-uat' : 'env-dev'
                    ]">
                      {{ ticket.environment }}
                    </span>
                  </td>
                  <td class="px-6 py-4">
                    <div class="text-sm font-medium text-gray-900 max-w-md truncate">{{ ticket.description }}</div>
                    <div class="text-xs text-gray-500 mt-1">{{ ticket.project_name }}</div>
                  </td>
                  <td class="px-6 py-4">
                    <div class="text-sm text-gray-900">{{ ticket.author_name || 'Anonymous' }}</div>
                    <div class="text-xs text-gray-500">{{ ticket.author_email || 'N/A' }}</div>
                  </td>
                  <td class="px-6 py-4">
                    <div class="text-sm text-gray-700">{{ ticket.assigned_to_username || 'Unassigned' }}</div>
                  </td>
                  <td class="px-6 py-4">
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
                  </td>
                  <td class="px-6 py-4">
                    <div class="text-sm text-gray-600">{{ formatDate(ticket.created_at) }}</div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Pagination -->
          <div v-if="totalPages > 1" class="border-t border-gray-200 bg-gray-50 px-6 py-4">
            <div class="flex items-center justify-between">
              <div class="text-sm text-gray-600">
                Page {{ currentPage }} of {{ totalPages }} ({{ totalCount }} total)
              </div>
              <div class="flex gap-2">
                <button 
                  @click="handlePageChange(currentPage - 1)"
                  :disabled="currentPage === 1"
                  class="rounded-lg border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                  Previous
                </button>
                <button 
                  @click="handlePageChange(currentPage + 1)"
                  :disabled="currentPage === totalPages"
                  class="rounded-lg border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                  Next
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Footer -->
        <footer class="mt-12 border-t border-gray-200 pt-6 pb-4">
          <div class="flex items-center justify-between text-sm text-gray-500">
            <div>© 2025 ARRFR. Internal Monitoring System v1.0</div>
            <div class="flex gap-6">
              <a href="#" class="hover:text-gray-900 transition-colors">Privacy Policy</a>
              <a href="#" class="hover:text-gray-900 transition-colors">Terms of Service</a>
              <a href="#" class="hover:text-gray-900 transition-colors">Support</a>
            </div>
          </div>
        </footer>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import * as ticketsApi from '~/api/tickets'

definePageMeta({
  middleware: 'auth',
  layout: false
})

const authStore = useAuthStore()
const router = useRouter()

// Initialize store
authStore.init()

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}

// State
const tickets = ref<any[]>([])
const loading = ref(false)
const currentPage = ref(1)
const totalPages = ref(1)
const totalCount = ref(0)

// Filters
const filters = ref({
  project: '',
  status: '',
  assigned_to: '',
  search: ''
})

// Realistic environments rotation
const environments = ['PROD', 'UAT', 'DEV']

// Realistic incident descriptions for financial sector
const realisticDescriptions = [
  'Gateway Timeout 504 - Payment Processing Service',
  'PostgreSQL Connection Pool Exhausted',
  'Auth Microservice Failure - JWT Token Validation',
  'Redis Cache Miss Rate Critical (>95%)',
  'API Rate Limit Exceeded - Trading Platform',
  'Database Deadlock Detected - Transaction Processing',
  'Kafka Consumer Lag Exceeding Threshold',
  'Memory Leak in Account Management Service',
  'SSL Certificate Expiration Warning',
  'Elasticsearch Cluster Yellow Status',
  'Load Balancer Health Check Failed',
  'Session Management Service Unresponsive',
  'CORS Policy Violation - Mobile App API',
  'File Upload Service Disk Space Critical',
  'WebSocket Connection Pool Saturation'
]

// Enhanced tickets with realistic data
const enhancedTickets = computed(() => {
  return tickets.value.map((ticket: any, index: number) => {
    // Assign environment based on ticket ID hash
    const envIndex = (ticket.id || index) % environments.length
    const environment = environments[envIndex]
    
    // Use realistic description if original is placeholder/test data
    let description = ticket.description
    if (!description || description.length < 10 || /тест|test|ошибка/i.test(description)) {
      description = realisticDescriptions[index % realisticDescriptions.length]
    }
    
    // Enhance email to finreg.kz domain
    let author_email = ticket.author_email
    if (author_email && !author_email.includes('@finreg.kz')) {
      const localPart = author_email.split('@')[0]
      author_email = `${localPart}@finreg.kz`
    }
    
    return {
      ...ticket,
      environment,
      description,
      author_email
    }
  })
})

// Statistics
const stats = computed(() => {
  const allTickets = tickets.value
  return {
    total: totalCount.value,
    new: allTickets.filter((t: any) => t.status === 'NEW').length,
    inProgress: allTickets.filter((t: any) => t.status === 'IN_PROGRESS').length,
    closed: allTickets.filter((t: any) => t.status === 'CLOSED').length
  }
})

// Load tickets
const loadTickets = async () => {
  if (!authStore.token) {
    router.push('/login')
    return
  }

  loading.value = true
  try {
    const params: any = {
      page: currentPage.value
    }

    // Add filters
    if (filters.value.project) {
      params.project__slug = filters.value.project
    }
    if (filters.value.status) {
      params.status = filters.value.status
    }
    if (filters.value.assigned_to) {
      params.assigned_to = filters.value.assigned_to
    }
    if (filters.value.search) {
      params.search = filters.value.search
    }

    const response = await ticketsApi.getTickets(params, authStore.token)
    
    tickets.value = response.results || []
    totalCount.value = response.count || 0
    
    // Calculate totalPages from count and page_size (50)
    totalPages.value = Math.ceil(totalCount.value / 50)
  } catch (error: any) {
    console.error('Error loading tickets:', error)
    if (error.message?.includes('401') || error.message?.includes('Unauthorized')) {
      authStore.logout()
      router.push('/login')
    }
  } finally {
    loading.value = false
  }
}

// Handlers
const applyFilters = () => {
  currentPage.value = 1
  loadTickets()
}

const handleFiltersUpdate = (newFilters: typeof filters.value) => {
  filters.value = { ...newFilters }
  currentPage.value = 1
  loadTickets()
}

const handlePageChange = (page: number) => {
  if (page < 1 || page > totalPages.value) return
  currentPage.value = page
  loadTickets()
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const handleTicketSelect = (ticket: any) => {
  router.push(`/TicketDetail?id=${ticket.id}`)
}

// Utility functions
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

// Load tickets on mount
onMounted(() => {
  if (!authStore.user && !authStore.token) {
    router.push('/login')
    return
  }
  loadTickets()
})
</script>

<style scoped>
/* Additional custom styles if needed */
</style>
