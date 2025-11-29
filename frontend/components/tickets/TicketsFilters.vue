<template>
  <div class="card mb-4">
    <div class="card-body">
      <div class="row g-3">
        <div class="col-md-3">
          <label for="projectFilter" class="form-label">Проект</label>
          <select
            id="projectFilter"
            v-model="localFilters.project"
            class="form-select"
            @change="emitUpdate"
          >
            <option value="">Все проекты</option>
            <option
              v-for="project in projects"
              :key="project.id"
              :value="project.slug"
            >
              {{ project.name }}
            </option>
          </select>
        </div>
        
        <div class="col-md-2">
          <label for="statusFilter" class="form-label">Статус</label>
          <select
            id="statusFilter"
            v-model="localFilters.status"
            class="form-select"
            @change="emitUpdate"
          >
            <option value="">Все статусы</option>
            <option value="NEW">Новая</option>
            <option value="IN_PROGRESS">В работе</option>
            <option value="CLOSED">Закрыта</option>
          </select>
        </div>
        
        <div class="col-md-2">
          <label for="assignedFilter" class="form-label">Ответственный</label>
          <select
            id="assignedFilter"
            v-model="localFilters.assigned_to"
            class="form-select"
            @change="emitUpdate"
          >
            <option value="">Все</option>
            <option
              v-for="user in staffUsers"
              :key="user.id"
              :value="user.id"
            >
              {{ user.username }}
            </option>
          </select>
        </div>
        
        <div class="col-md-3">
          <label for="searchFilter" class="form-label">Поиск</label>
          <input
            id="searchFilter"
            v-model="localFilters.search"
            type="text"
            class="form-control"
            placeholder="ID, описание, email..."
            @input="emitUpdate"
          />
        </div>
        
        <div class="col-md-2 d-flex align-items-end">
          <button
            class="btn btn-outline-secondary w-100"
            @click="resetFilters"
            type="button"
          >
            Сбросить
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import * as projectsApi from '~/api/projects'
import * as usersApi from '~/api/users'

interface Props {
  filters: {
    project?: string
    status?: string
    assigned_to?: string
    search?: string
  }
}

const props = defineProps<Props>()

const emit = defineEmits<{
  update: [filters: typeof props.filters]
}>()

const authStore = useAuthStore()
const localFilters = ref({ ...props.filters })
const projects = ref([])
const staffUsers = ref([])

// Загружаем проекты
onMounted(async () => {
  try {
    const response = await projectsApi.getProjects()
    projects.value = response.results || []
  } catch (error) {
    console.error('Ошибка загрузки проектов:', error)
  }
  
  // Загружаем staff пользователей с токеном
  if (authStore.token) {
    try {
      staffUsers.value = await usersApi.getStaffUsers(authStore.token)
    } catch (error) {
      console.error('Ошибка загрузки пользователей:', error)
    }
  }
})

// Следим за изменениями props
watch(() => props.filters, (newFilters) => {
  localFilters.value = { ...newFilters }
}, { deep: true })

const emitUpdate = () => {
  emit('update', { ...localFilters.value })
}

const resetFilters = () => {
  localFilters.value = {
    project: '',
    status: '',
    assigned_to: '',
    search: ''
  }
  emit('update', { ...localFilters.value })
}
</script>

