import { API_ENDPOINTS } from './backendEndpoints.js'
import { apiGet, apiPost } from './client.js'

/**
 * Модуль для работы с комментариями
 */

/**
 * Получить список комментариев
 * @param {Object} params - Параметры (ticket - фильтр по ticket_id, page и т.д.)
 * @param {string} accessToken - Токен авторизации
 * @returns {Promise<{count: number, results: Array}>}
 */
export async function getComments(params = {}, accessToken) {
  return apiGet(API_ENDPOINTS.comments, accessToken, params)
}

/**
 * Создать комментарий
 * @param {Object} commentData - Данные комментария
 * @param {number} commentData.ticket - ID заявки
 * @param {string} commentData.text - Текст комментария
 * @param {string} accessToken - Токен авторизации
 * @returns {Promise<Object>}
 */
export async function createComment(commentData, accessToken) {
  return apiPost(API_ENDPOINTS.comments, commentData, accessToken)
}

