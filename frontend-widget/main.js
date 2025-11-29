import { createApp } from 'vue';
import App from './app/App.vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import { initProjectSlug } from './app/projectConfig';

export const WIDGET_VERSION = '1.0.0';

export default function mountWidget(selector = '#widget-root') {
  initProjectSlug();
  let el = document.querySelector(selector);
  if (!el) {
    el = document.createElement('div');
    el.id = selector.replace('#', '');
    document.body.appendChild(el);
  }
  createApp(App).mount(el);
}
