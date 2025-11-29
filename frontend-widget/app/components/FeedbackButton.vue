<template>
  <div>
    <button
      class="feedback-btn"
      :aria-pressed="isOpen"
      @click="isOpen = true"
    >
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="12" cy="12" r="12" fill="white"/>
        <text x="12" y="17" text-anchor="middle" font-size="16" fill="#0d6efd" font-family="Arial" dominant-baseline="middle">?</text>
      </svg>
    </button>
    <FeedbackModal v-if="isOpen" @close="isOpen = false" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import FeedbackModal from './FeedbackModal.vue';
const isOpen = ref(false);
</script>

<style scoped>
.feedback-btn {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 2147483647;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: #0d6efd;
  color: #fff;
  border: none;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: box-shadow 0.2s;
  outline: none;
  padding: 0;
}
.feedback-btn:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.18);
}
.feedback-btn svg {
  pointer-events: none;
}
</style>
