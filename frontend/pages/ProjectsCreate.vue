<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6 col-lg-5">
        <div class="card shadow">
          <div class="card-body p-4">
            <h2 class="mb-4 text-center">Создать новый проект</h2>
            <form @submit.prevent="createProjectHandler">
              <div v-if="error" class="alert alert-danger">
                {{ error }}
              </div>
              <div class="mb-3">
                <label class="form-label">Название проекта</label>
                <input v-model="name" class="form-control" required maxlength="255" />
              </div>
              <div class="mb-3">
                <label class="form-label">Slug (латиницей, уникально)</label>
                <input v-model="slug" class="form-control" required maxlength="255" pattern="[a-zA-Z0-9-_]+" />
              </div>
              <div class="form-check mb-3">
                <input v-model="isActive" class="form-check-input" type="checkbox" id="activeCheck" />
                <label class="form-check-label" for="activeCheck">Активен</label>
              </div>
              <button class="btn btn-primary w-100" :disabled="loading">
                <span v-if="loading" class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                {{ loading ? 'Создание...' : 'Создать' }}
              </button>
            </form>
            <div v-if="script" class="alert alert-success mt-4">
              <div>Проект создан! Скопируйте этот код для вставки виджета на сайт:</div>
              <pre class="bg-light p-2 border rounded"><code>{{ script }}</code></pre>
              <button class="btn btn-outline-secondary btn-sm mt-2" @click="copyScript">Скопировать</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { createProject } from '~/api/projects'
import { useAuthStore } from '~/stores/auth'


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
      script.value = `<script src="https://unpkg.com/vue@3/dist/vue.global.prod.js"></script>\n<script src="${widgetHost}" data-project-slug="${data.slug}"></script>`;
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
