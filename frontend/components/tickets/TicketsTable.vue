<template>
  <div class="card">
    <div class="card-body">
      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Загрузка...</span>
        </div>
      </div>
      
      <div v-else-if="tickets.length === 0" class="text-center py-5 text-muted">
        Заявки не найдены
      </div>
      
      <div v-else class="table-responsive">
        <table class="table table-hover table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Проект</th>
              <th>Статус</th>
              <th>Автор</th>
              <th>Email</th>
              <th>Описание</th>
              <th>Ответственный</th>
              <th>Создана</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="ticket in tickets"
              :key="ticket.id"
              @click="handleSelect(ticket)"
              style="cursor: pointer;"
            >
              <td>
                <strong>{{ ticket.ticket_id }}</strong>
              </td>
              <td>{{ ticket.project_name || '-' }}</td>
              <td>
                <span :class="getStatusBadgeClass(ticket.status)">
                  {{ getStatusLabel(ticket.status) }}
                </span>
              </td>
              <td>{{ ticket.author_name || '-' }}</td>
              <td>{{ ticket.author_email || '-' }}</td>
              <td>
                <div class="text-truncate" style="max-width: 200px;">
                  {{ ticket.description }}
                </div>
              </td>
              <td>{{ ticket.assigned_to_username || '-' }}</td>
              <td>{{ formatDate(ticket.created_at) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Ticket {
  id: number
  ticket_id: string
  project_name?: string
  status: string
  author_name?: string
  author_email?: string
  description: string
  assigned_to_username?: string
  created_at: string
}

interface Props {
  tickets: Ticket[]
  loading?: boolean
}

defineProps<Props>()

const emit = defineEmits<{
  select: [ticket: Ticket]
}>()

const handleSelect = (ticket: Ticket) => {
  emit('select', ticket)
}

const getStatusLabel = (status: string) => {
  const labels: Record<string, string> = {
    NEW: 'Новая',
    IN_PROGRESS: 'В работе',
    CLOSED: 'Закрыта'
  }
  return labels[status] || status
}

const getStatusBadgeClass = (status: string) => {
  const classes: Record<string, string> = {
    NEW: 'badge bg-danger',
    IN_PROGRESS: 'badge bg-warning',
    CLOSED: 'badge bg-success'
  }
  return classes[status] || 'badge bg-secondary'
}

const formatDate = (dateString: string) => {
  if (!dateString) return '-'
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>

