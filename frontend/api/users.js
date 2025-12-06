import { API_ENDPOINTS } from './backendEndpoints.js'
import { apiGet } from './client.js'

/**
 * Модуль для работы с пользователями
 */

/**
 * Получить текущего пользователя
 * @param {string} accessToken - Токен авторизации
 * @returns {Promise<Object>}
 */
export async function getCurrentUser(accessToken) {
  return apiGet(API_ENDPOINTS.currentUser, accessToken)
}

/**
 * Получить список staff пользователей (сотрудников)
 * @param {string} accessToken - Токен авторизации
 * @returns {Promise<Array>}
 */
export async function getStaffUsers(accessToken = null) {
  try {
    return apiGet(API_ENDPOINTS.staffUsers, accessToken)
  } catch (error) {
    // Если эндпоинт не существует, возвращаем пустой массив
    console.warn('Эндпоинт /api/users/staff/ не найден, используем пустой список')
    return []
  }
}

