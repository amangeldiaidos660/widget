import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import { initDB } from './services/db'

;(async () => {
	// Инициализируем sqlite (sql.js) и структуру таблиц перед монтированием приложения
	try {
		await initDB()
	} catch (err) {
		// Если инициализация провалилась, выводим в консоль — приложение продолжит запуск
		console.error('DB init error:', err)
	}

	createApp(App).mount('#app')
})()
