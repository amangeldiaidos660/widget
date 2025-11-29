import { ref } from 'vue';

// Глобальный ref для projectSlug
export const projectSlug = ref('');

// Инициализация projectSlug
export function initProjectSlug() {
  // 1. window.FEEDBACK_CONFIG?.projectSlug
  if (window.FEEDBACK_CONFIG && window.FEEDBACK_CONFIG.projectSlug) {
    projectSlug.value = window.FEEDBACK_CONFIG.projectSlug;
    return;
  }
  // 2. data-project-slug на <script src="widget.umd.js">
  const scripts = document.getElementsByTagName('script');
  for (const s of scripts) {
    if (s.src && s.src.includes('widget.umd')) {
      const slug = s.getAttribute('data-project-slug');
      if (slug) {
        projectSlug.value = slug;
        return;
      }
    }
  }
  // 3. fallback
  projectSlug.value = '';
}
