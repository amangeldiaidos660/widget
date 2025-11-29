<template>
  <div class="feedback-modal-backdrop" @click.self="close">
    <div class="modal-dialog modal-lg feedback-modal-dialog">
      <div class="modal-content feedback-modal-content">
        <div class="modal-header feedback-modal-header">
          <h5 class="modal-title">Сообщить о проблеме</h5>
          <button type="button" class="btn-close" aria-label="Close" @click="close"></button>
        </div>
        <form @submit.prevent="submit">
          <div class="modal-body feedback-modal-body">
            <div class="mb-3">
              <label class="form-label">Ваше имя</label>
              <input type="text" class="form-control" v-model="name" autocomplete="name" />
            </div>
            <div class="mb-3">
              <label class="form-label">Email или телефон <span style="color:red">*</span></label>
              <input type="text" class="form-control" v-model="contact" required />
            </div>
            <div class="mb-3">
              <label class="form-label">Что произошло? <span style="color:red">*</span></label>
              <textarea class="form-control" v-model="description" rows="4" required minlength="10"></textarea>
              <div v-if="description && description.length < 10" class="form-text text-danger">Минимум 10 символов</div>
            </div>
          </div>
          <div class="modal-footer feedback-modal-footer">
            <button type="button" class="btn btn-secondary" @click="close">Отмена</button>
            <button type="submit" class="btn btn-primary" :disabled="!canSubmit">Отправить</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { projectSlug } from '../projectConfig';
const emit = defineEmits(['close']);
const name = ref('');
const contact = ref('');
const description = ref('');

onMounted(() => {
  name.value = localStorage.getItem('name') || '';
  contact.value = localStorage.getItem('contact') || '';
});

const close = () => emit('close');
const canSubmit = computed(() => contact.value && description.value && description.value.length >= 10);
const submit = () => {
  localStorage.setItem('name', name.value);
  localStorage.setItem('contact', contact.value);
  console.log({ name: name.value, contact: contact.value, description: description.value, project_slug: projectSlug.value });
  close();
};
</script>

<style scoped>
.feedback-modal-backdrop {
  position: fixed !important;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.5) !important;
  z-index: 2147483647 !important;
  display: flex;
  align-items: center;
  justify-content: center;
}
.feedback-modal-dialog {
  max-width: 700px !important;
  width: 100%;
}
.feedback-modal-content {
  border-radius: 12px !important;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0,0,0,0.25) !important;
}
.feedback-modal-header, .feedback-modal-footer {
  background: #f8f9fa !important;
}
.btn-close {
  background: none !important;
  border: none !important;
  font-size: 1.5rem !important;
  opacity: 0.7 !important;
}
.btn-close:hover {
  opacity: 1 !important;
}
</style>
