import { API_ENDPOINTS } from './backendEndpoints.js'
import { apiGet } from './client.js'

/**
 * Модуль для работы с пользователями
 */

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

