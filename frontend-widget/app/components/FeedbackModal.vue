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
const loading = ref(false);

onMounted(() => {
  name.value = localStorage.getItem('name') || '';
  contact.value = localStorage.getItem('contact') || '';
});

const close = () => emit('close');
const canSubmit = computed(() => contact.value && description.value && description.value.length >= 10 && !loading.value);
const submit = async () => {
  loading.value = true;
  try {
    const payload = {
      project_slug: projectSlug.value,
      author_name: name.value.trim() || null,
      author_email: contact.value.trim() || null,
      author_login: '',
      description: description.value,
      page_url: window.location.href,
      user_agent: navigator.userAgent,
      screen_resolution: `${window.screen.width}x${window.screen.height}`,
      console_logs: JSON.stringify(window.__FEEDBACK_LOGS__ || []),
      network_errors: JSON.stringify(window.__FEEDBACK_NETWORK_ERRORS__ || []),
      js_errors: JSON.stringify(window.__FEEDBACK_JS_ERRORS__ || [])
    };
    console.log('Отправляем payload:', payload);
    const response = await fetch('http://localhost:8000/api/tickets/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const text = await response.text();
    let data;
    try { data = JSON.parse(text); } catch { data = text; }
    console.log('Ответ сервера:', data);
    if (response.ok && data.ticket_id) {
      localStorage.setItem('name', name.value);
      localStorage.setItem('contact', contact.value);
      close();
      setTimeout(() => {
        alert(`Ваша заявка №${data.ticket_id} принята! Спасибо!`);
      }, 200);
    } else {
      alert('Ошибка при отправке заявки: ' + JSON.stringify(data));
    }
  } catch (e) {
    alert('Ошибка сети. Попробуйте позже.');
    console.error(e);
  } finally {
    loading.value = false;
  }
};
</script>

