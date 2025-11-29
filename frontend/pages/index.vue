<template>
  <div class="container-fluid mt-4">
    <h1 class="mb-4">Портал заявок</h1>
    
    <!-- Статистика -->
    <TicketsStats :stats="stats" />
    
    <!-- Фильтры -->
    <TicketsFilters
      :filters="filters"
      @update="handleFiltersUpdate"
    />
    
    <!-- Таблица -->
    <TicketsTable
      :tickets="tickets"
      :loading="loading"
      @select="handleTicketSelect"
    />
    
    <!-- Пагинация -->
    <div class="mt-4">
      <TicketsPagination
        :current-page="currentPage"
        :total-pages="totalPages"
        @change="handlePageChange"
      />
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

// Инициализируем store
authStore.init()

// Состояние
const tickets = ref([])
const loading = ref(false)
const currentPage = ref(1)
const totalPages = ref(1)
const totalCount = ref(0)

// Фильтры
const filters = ref({
  project: '',
  status: '',
  assigned_to: '',
  search: ''
})

// Статистика
const stats = computed(() => {
  // Подсчитываем статистику из загруженных данных
  // В реальном приложении лучше получать отдельным запросом
  const allTickets = tickets.value
  return {
    total: totalCount.value,
    new: allTickets.filter((t: any) => t.status === 'NEW').length,
    inProgress: allTickets.filter((t: any) => t.status === 'IN_PROGRESS').length,
    closed: allTickets.filter((t: any) => t.status === 'CLOSED').length
  }
})

// Загрузка заявок
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

    // Добавляем фильтры
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
    
    // Вычисляем totalPages из count и page_size (50)
    totalPages.value = Math.ceil(totalCount.value / 50)
  } catch (error: any) {
    console.error('Ошибка загрузки заявок:', error)
    if (error.message?.includes('401') || error.message?.includes('Unauthorized')) {
      authStore.logout()
      router.push('/login')
    }
  } finally {
    loading.value = false
  }
}

// Обработчики
const handleFiltersUpdate = (newFilters: typeof filters.value) => {
  filters.value = { ...newFilters }
  currentPage.value = 1 // Сбрасываем на первую страницу
  loadTickets()
}

const handlePageChange = (page: number) => {
  currentPage.value = page
  loadTickets()
  // Прокрутка вверх
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const handleTicketSelect = (ticket: any) => {
  // Переход на страницу заявки (пока 404, но роут готовим)
  router.push(`/tickets/${ticket.id}`)
}

// Загружаем заявки при монтировании
onMounted(() => {
  if (!authStore.user && !authStore.token) {
    router.push('/login')
    return
  }
  loadTickets()
})
</script>

