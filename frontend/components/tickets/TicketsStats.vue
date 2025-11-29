<template>
  <div class="row mb-4">
    <div class="col-md-3 mb-3 mb-md-0">
      <div class="card text-white bg-primary">
        <div class="card-body">
          <h5 class="card-title">Все заявки</h5>
          <h2 class="mb-0">{{ stats.total || 0 }}</h2>
        </div>
      </div>
    </div>
    <div class="col-md-3 mb-3 mb-md-0">
      <div class="card text-white bg-danger">
        <div class="card-body">
          <h5 class="card-title">Новые</h5>
          <h2 class="mb-0">{{ stats.new || 0 }}</h2>
        </div>
      </div>
    </div>
    <div class="col-md-3 mb-3 mb-md-0">
      <div class="card text-white bg-warning">
        <div class="card-body">
          <h5 class="card-title">В работе</h5>
          <h2 class="mb-0">{{ stats.inProgress || 0 }}</h2>
        </div>
      </div>
    </div>
    <div class="col-md-3">
      <div class="card text-white bg-success">
        <div class="card-body">
          <h5 class="card-title">Закрыто</h5>
          <h2 class="mb-0">{{ stats.closed || 0 }}</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  stats: {
    total?: number
    new?: number
    inProgress?: number
    closed?: number
  }
}

defineProps<Props>()
</script>

