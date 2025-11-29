<template>
  <div>
    <div class="row">
      <div class="col-12">
        <h1 class="mb-4">Добро пожаловать в портал заявок</h1>
        <p class="lead">Вы успешно вошли в систему</p>
        <div v-if="authStore.user" class="card mt-4">
          <div class="card-body">
            <h5 class="card-title">Информация о пользователе</h5>
            <p class="card-text">
              <strong>Логин:</strong> {{ authStore.user.username }}<br>
              <span v-if="authStore.user.email">
                <strong>Email:</strong> {{ authStore.user.email }}
              </span>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: 'auth',
  layout: 'default'
})

const authStore = useAuthStore()
</script>

