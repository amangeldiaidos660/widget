<template>
  <div>
    <NuxtRouteAnnouncer />
    <NuxtWelcome />
    <FeedbackButton />
  </div>
</template>

<script setup>
import FeedbackButton from './components/FeedbackButton.vue';
</script>

<style>
/* Глобальная защита кнопки от reset-стилей */
.feedback-btn {
  all: unset;
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
