<template>
  <NuxtLayout>
    <div class="p-8">
      <div class="max-w-3xl mx-auto">
        <!-- Page Header -->
        <div class="mb-8">
          <h1 class="text-3xl font-bold text-gray-900 mb-2">{{ t.projects.title }}</h1>
          <p class="text-gray-600">{{ t.projects.subtitle }}</p>
        </div>

        <!-- Form Card -->
        <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-8">
          <form @submit.prevent="createProjectHandler" class="space-y-6">
            <div v-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4 flex items-start gap-3">
              <svg class="h-5 w-5 text-red-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <div class="text-sm text-red-800">{{ error }}</div>
            </div>

            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">
                {{ t.projects.projectName }}
                <span class="text-red-500">*</span>
              </label>
              <input 
                v-model="name" 
                type="text"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all" 
                :placeholder="t.projects.enterProjectName"
                required 
                maxlength="255" />
              <p class="mt-1 text-sm text-gray-500">{{ t.projects.required }}</p>
            </div>

            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">
                {{ t.projects.projectSlug }}
                <span class="text-red-500">*</span>
              </label>
              <input 
                v-model="slug" 
                type="text"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all font-mono" 
                :placeholder="t.projects.enterSlug"
                required 
                maxlength="255" 
                pattern="[a-zA-Z0-9-_]+" />
              <p class="mt-1 text-sm text-gray-500">{{ t.projects.slugHelp }}</p>
            </div>

            <div class="flex items-center gap-3 p-4 bg-gray-50 rounded-lg">
              <input 
                v-model="isActive" 
                class="h-5 w-5 text-blue-600 border-gray-300 rounded focus:ring-blue-500" 
                type="checkbox" 
                id="activeCheck" />
              <label class="text-sm font-medium text-gray-700 cursor-pointer" for="activeCheck">
                {{ t.projects.activateImmediately }}
              </label>
            </div>

            <div class="flex gap-3 pt-4">
              <button 
                type="submit"
                class="flex-1 bg-blue-600 text-white font-semibold py-3 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                :disabled="loading"
              >
                <svg v-if="loading" class="animate-spin h-5 w-5" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span>{{ loading ? t.projects.creating : t.projects.createProject }}</span>
              </button>
              <NuxtLink 
                to="/"
                class="px-6 py-3 border border-gray-300 rounded-lg font-semibold text-gray-700 hover:bg-gray-50 transition-colors"
              >
                {{ t.common.cancel }}
              </NuxtLink>
            </div>
          </form>

          <!-- Success Message with Widget Code -->
          <div v-if="script" class="mt-8 border-t border-gray-200 pt-8">
            <div class="bg-green-50 border border-green-200 rounded-lg p-6">
              <div class="flex items-start gap-3 mb-4">
                <svg class="h-6 w-6 text-green-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <div>
                  <h3 class="text-lg font-bold text-green-900 mb-1">{{ t.projects.projectCreated }}</h3>
                  <p class="text-sm text-green-700">{{ t.projects.widgetInstructions }}</p>
                </div>
              </div>

              <div class="bg-slate-900 rounded-lg p-4 mb-4 overflow-x-auto">
                <code class="text-sm text-green-400 font-mono" v-html="script"></code>
              </div>

              <button 
                @click="copyScript"
                class="w-full bg-green-600 text-white font-semibold py-2.5 rounded-lg hover:bg-green-700 transition-colors flex items-center justify-center gap-2"
              >
                <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
                {{ t.projects.copyWidgetCode }}
              </button>
            </div>
          </div>
        </div>

        <!-- Info Card -->
        <div class="mt-6 bg-blue-50 border border-blue-200 rounded-xl p-6">
          <div class="flex items-start gap-3">
            <svg class="h-6 w-6 text-blue-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <div class="text-sm text-blue-900">
              <p class="font-semibold mb-2">{{ t.projects.integrationGuide }}</p>
              <ul class="list-disc list-inside space-y-1 text-blue-800">
                <li>{{ t.projects.autoTracking }}</li>
                <li>{{ t.projects.appearInDashboard }}</li>
                <li>{{ t.projects.submitFeedback }}</li>
                <li>{{ t.projects.automaticDiagnostics }}</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { createProject } from '~/api/projects'
import { useAuthStore } from '~/stores/auth'
import { useLanguageStore } from '~/stores/language'

const langStore = useLanguageStore()
const t = computed(() => langStore.t)

const name = ref('')
const slug = ref('')
const isActive = ref(true)
const loading = ref(false)
const script = ref('')
const error = ref('')
const authStore = useAuthStore()

const createProjectHandler = async () => {
  loading.value = true
  error.value = ''
  script.value = ''
  try {
    const data = await createProject(
      { name: name.value, slug: slug.value, is_active: isActive.value },
      authStore.token
    )
    if (data.slug) {
      let widgetHost = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
        ? 'http://localhost:3000/widget.umd.v1.0.0.js'
        : 'https://neurocity.app/widget.umd.v1.0.0.js';
      script.value = `&lt;script src="https://unpkg.com/vue@3/dist/vue.global.prod.js"&gt;&lt;/script&gt;
      &lt;script src="${widgetHost}" data-project-slug="${data.slug}"&gt;&lt;/script&gt;`;

    } else {
      error.value = data.detail || JSON.stringify(data)
    }
  } catch (e: any) {
    error.value = e.message || 'Ошибка сети или сервера'
  } finally {
    loading.value = false
  }
}

const copyScript = () => {
  if (script.value) {
    navigator.clipboard.writeText(script.value)
  }
}
</script>
