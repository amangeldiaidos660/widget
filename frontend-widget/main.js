import { createApp } from 'vue';
import App from './app/App.vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import { initProjectSlug } from './app/projectConfig';

// --- Диагностика: глобальные массивы для логов ---
window.__FEEDBACK_LOGS__ = [];
window.__FEEDBACK_NETWORK_ERRORS__ = [];
window.__FEEDBACK_JS_ERRORS__ = [];

const origError = console.error;
const origWarn = console.warn;
console.error = (...args) => {
  window.__FEEDBACK_LOGS__.push({ type: 'error', time: Date.now(), data: args.map(String) });
  origError.apply(console, args);
};
console.warn = (...args) => {
  window.__FEEDBACK_LOGS__.push({ type: 'warn', time: Date.now(), data: args.map(String) });
  origWarn.apply(console, args);
};
window.addEventListener('error', (e) => {
  window.__FEEDBACK_JS_ERRORS__.push({
    message: e.message,
    file: e.filename,
    line: e.lineno,
    column: e.colno,
    stack: e.error?.stack || null,
    time: Date.now()
  });
});
window.addEventListener('unhandledrejection', (e) => {
  window.__FEEDBACK_JS_ERRORS__.push({
    type: 'unhandledrejection',
    reason: e.reason?.message || String(e.reason),
    stack: e.reason?.stack || null,
    time: Date.now()
  });
});
// --- END диагностика ---

export const WIDGET_VERSION = '1.0.0';

export default function mountWidget(selector = '#widget-root') {
  // Подключаем стили виджета, если не подключены
  (function(){
    var cssId = 'widget-feedback-css';
    if (!document.getElementById(cssId)) {
      var link = document.createElement('link');
      link.id = cssId;
      link.rel = 'stylesheet';
      link.type = 'text/css';
      link.href = './widget-feedback.css';
      document.head.appendChild(link);
    }
  })();

  initProjectSlug();
  let el = document.querySelector(selector);
  if (!el) {
    el = document.createElement('div');
    el.id = selector.replace('#', '');
    document.body.appendChild(el);
  }
  createApp(App).mount(el);
}
