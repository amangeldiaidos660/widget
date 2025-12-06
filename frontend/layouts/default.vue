<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Sidebar -->
    <aside class="fixed left-0 top-0 z-40 h-screen w-64 bg-slate-900 text-white transition-transform">
      <div class="flex h-full flex-col">
        <!-- Logo -->
        <div class="flex h-16 items-center justify-center border-b border-slate-800 px-6">
          <div class="flex items-center gap-3">
            <!-- Вставьте ваш логотип ARRFR здесь -->
            <div class="h-10 w-10 rounded-lg bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center">
              <!-- SVG placeholder - замените на ваш логотип -->
              <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <div>
              <div class="text-sm font-bold">ARRFR</div>
              <div class="text-xs text-slate-400">Helpdesk System</div>
            </div>
          </div>
        </div>

        <!-- Navigation -->
        <nav class="flex-1 space-y-1 px-3 py-4">
          <NuxtLink to="/" class="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium text-slate-300 hover:bg-slate-800 hover:text-white transition-colors" active-class="bg-slate-800 text-white">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            <span>{{ langStore.t.common.dashboard }}</span>
          </NuxtLink>
          <NuxtLink to="/tickets" class="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium text-slate-300 hover:bg-slate-800 hover:text-white transition-colors" active-class="bg-slate-800 text-white">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
            <span>{{ langStore.t.common.tickets }}</span>
          </NuxtLink>
          <NuxtLink to="/ProjectsCreate" class="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium text-slate-300 hover:bg-slate-800 hover:text-white transition-colors" active-class="bg-slate-800 text-white">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
            </svg>
            <span>{{ langStore.t.common.projects }}</span>
          </NuxtLink>
          <NuxtLink to="/reports" class="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium text-slate-300 hover:bg-slate-800 hover:text-white transition-colors" active-class="bg-slate-800 text-white">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            <span>{{ langStore.t.common.reports }}</span>
          </NuxtLink>
          <NuxtLink to="/status" class="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium text-slate-300 hover:bg-slate-800 hover:text-white transition-colors" active-class="bg-slate-800 text-white">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>{{ langStore.t.common.status }}</span>
          </NuxtLink>
          <NuxtLink to="/profile" class="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium text-slate-300 hover:bg-slate-800 hover:text-white transition-colors" active-class="bg-slate-800 text-white">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
            <span>{{ langStore.t.common.profile }}</span>
          </NuxtLink>
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
            <span class="font-semibold text-gray-900">{{ breadcrumb }}</span>
          </div>

          <!-- Right Side -->
          <div class="flex items-center gap-4">
            <!-- Language Switcher -->
            <div class="flex items-center gap-1 rounded-lg border border-gray-300 p-1">
              <button 
                @click="switchLanguage('kz')" 
                :class="langStore.currentLang === 'kz' ? 'bg-blue-600 text-white' : 'text-gray-600 hover:bg-gray-100'"
                class="px-3 py-1 text-xs font-medium rounded-md transition-colors"
              >
                KZ
              </button>
              <button 
                @click="switchLanguage('ru')" 
                :class="langStore.currentLang === 'ru' ? 'bg-blue-600 text-white' : 'text-gray-600 hover:bg-gray-100'"
                class="px-3 py-1 text-xs font-medium rounded-md transition-colors"
              >
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
      <main class="min-h-screen bg-gray-50/50">
        <slot />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/stores/auth'
import { useLanguageStore } from '~/stores/language'

const authStore = useAuthStore()
const langStore = useLanguageStore()
const router = useRouter()
const route = useRoute()

// Initialize language
onMounted(() => {
  langStore.init()
})

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}

const switchLanguage = (lang: 'kz' | 'ru') => {
  langStore.setLanguage(lang)
}

const breadcrumb = computed(() => {
  const path = route.path
  const t = langStore.t
  
  if (path === '/') return t.common.dashboard
  if (path.includes('ticket')) return t.tickets.title
  if (path.includes('project')) return t.common.projects
  if (path.includes('status')) return t.status.title
  if (path.includes('reports')) return t.common.reports
  if (path.includes('profile')) return t.common.profile
  
  return t.common.dashboard
})
</script>
