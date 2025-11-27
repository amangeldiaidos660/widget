<template>
  <div>
    <p v-if="status === 'ok'">API OK</p>
    <p v-else>API Error</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchHealth } from '~/api/health.js'

const status = ref(null)

onMounted(async () => {
  try {
    const data = await fetchHealth()
    status.value = data.status
  } catch {
    status.value = null
  }
})
</script>
