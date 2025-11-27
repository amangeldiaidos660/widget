// backendEndpoints.js
// Главная точка входа для всех API-эндпоинтов и базового URL backend

export const BACKEND_BASE_URL = 'http://localhost:8000'

export const API_ENDPOINTS = {
  health: `${BACKEND_BASE_URL}/api/health/`,
  // Добавляйте новые эндпоинты здесь
}
