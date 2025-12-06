<template>
  <NuxtLayout>
    <div class="p-8">
      <div class="max-w-4xl mx-auto">
        <!-- Page Header -->
        <div class="mb-8">
          <h1 class="text-3xl font-bold text-gray-900 mb-2">{{ t.status.title }}</h1>
          <p class="text-gray-600">{{ t.status.subtitle }}</p>
        </div>

        <!-- Overall Status Banner -->
        <div :class="[
          'rounded-xl border shadow-sm p-6 mb-6',
          apiHealth.status === 'ok' ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'
        ]">
          <div class="flex items-center gap-4">
            <div :class="[
              'h-16 w-16 rounded-full flex items-center justify-center',
              apiHealth.status === 'ok' ? 'bg-green-100' : 'bg-red-100'
            ]">
              <svg v-if="apiHealth.status === 'ok'" class="h-10 w-10 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <svg v-else class="h-10 w-10 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <div>
              <h2 :class="[
                'text-2xl font-bold',
                apiHealth.status === 'ok' ? 'text-green-900' : 'text-red-900'
              ]">
                {{ apiHealth.status === 'ok' ? t.status.allSystemsOperational : 'Системные проблемы' }}
              </h2>
              <p :class="apiHealth.status === 'ok' ? 'text-green-700' : 'text-red-700'">
                {{ apiHealth.status === 'ok' ? 'Все сервисы работают нормально' : 'Обнаружены проблемы с сервисами' }}
              </p>
            </div>
            <div class="ml-auto">
              <button 
                @click="checkHealth"
                :disabled="loading"
                class="px-4 py-2 bg-white border border-gray-300 rounded-lg text-sm font-medium hover:bg-gray-50 transition-colors disabled:opacity-50"
              >
                <svg v-if="loading" class="animate-spin h-5 w-5 inline" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span v-else>{{ t.common.loading === loading ? 'Обновить' : 'Обновить' }}</span>
              </button>
            </div>
          </div>
        </div>

        <!-- API Status Component -->
        <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-8 mb-6">
          <ApiStatus />
        </div>

        <!-- Additional Status Info -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-6">
            <div class="flex items-center gap-3 mb-3">
              <div :class="[
                'h-10 w-10 rounded-lg flex items-center justify-center',
                apiHealth.status === 'ok' ? 'bg-green-100' : 'bg-red-100'
              ]">
                <svg :class="apiHealth.status === 'ok' ? 'text-green-600' : 'text-red-600'" class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <div>
                <div class="text-2xl font-bold text-gray-900">{{ uptime }}</div>
                <div class="text-sm text-gray-500">{{ t.status.uptime }}</div>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-6">
            <div class="flex items-center gap-3 mb-3">
              <div class="h-10 w-10 rounded-lg bg-blue-100 flex items-center justify-center">
                <svg class="h-6 w-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <div>
                <div class="text-2xl font-bold text-gray-900">{{ responseTime }}ms</div>
                <div class="text-sm text-gray-500">{{ t.status.responseTime }}</div>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-6">
            <div class="flex items-center gap-3 mb-3">
              <div class="h-10 w-10 rounded-lg bg-purple-100 flex items-center justify-center">
                <svg class="h-6 w-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
              </div>
              <div>
                <div class="text-2xl font-bold text-gray-900">{{ apiHealth.status === 'ok' ? '100%' : '0%' }}</div>
                <div class="text-sm text-gray-500">{{ t.status.security }}</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Last Check Info -->
        <div class="mt-6 text-center text-sm text-gray-500">
          Последняя проверка: {{ lastCheckTime }}
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useLanguageStore } from '~/stores/language'
import { fetchHealth } from '~/api/health'

const langStore = useLanguageStore()
const t = computed(() => langStore.t)

const loading = ref(false)
const apiHealth = ref({ status: 'unknown' })
const responseTime = ref(0)
const uptime = ref('99.9%')
const lastCheckTime = ref('')
let intervalId = null

const checkHealth = async () => {
  loading.value = true
  const startTime = performance.now()
  
  try {
    const response = await fetchHealth()
    const endTime = performance.now()
    
    apiHealth.value = response
    responseTime.value = Math.round(endTime - startTime)
    
    // Рассчитываем uptime (простая логика)
    if (response.status === 'ok') {
      uptime.value = '99.9%'
    } else {
      uptime.value = '0%'
    }
    
    lastCheckTime.value = new Date().toLocaleString('ru-RU', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    })
  } catch (error) {
    console.error('Health check failed:', error)
    apiHealth.value = { status: 'error' }
    responseTime.value = 0
    uptime.value = '0%'
    lastCheckTime.value = new Date().toLocaleString('ru-RU')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  checkHealth()
  // Проверяем здоровье каждые 30 секунд
  intervalId = setInterval(checkHealth, 30000)
})

onUnmounted(() => {
  if (intervalId) {
    clearInterval(intervalId)
  }
})
</script>
