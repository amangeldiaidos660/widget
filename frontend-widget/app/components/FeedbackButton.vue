<template>
  <div>
    <button
      class="feedback-btn"
      :aria-pressed="isOpen"
      @click="isOpen = true"
      title="Обратная связь"
    >
      <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="16" cy="16" r="15" fill="#fff" stroke="#0d6efd" stroke-width="2"/>
        <text x="16" y="21" text-anchor="middle" font-size="20" fill="#0d6efd" font-family="Arial" dominant-baseline="middle" font-weight="bold">?</text>
      </svg>
    </button>
    <transition name="fade-modal">
      <FeedbackModal v-if="isOpen" @close="isOpen = false" />
    </transition>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import FeedbackModal from './FeedbackModal.vue';
const isOpen = ref(false);
</script>

