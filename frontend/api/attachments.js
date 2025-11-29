import { API_ENDPOINTS } from './backendEndpoints.js'
import { apiGet } from './client.js'

/**
 * Модуль для работы с вложениями (read-only)
 */

/**
 * Получить список вложений
 * @param {Object} params - Параметры (ticket - фильтр по ticket_id, page и т.д.)
 * @param {string} [accessToken] - Токен авторизации (опционально)
 * @returns {Promise<{count: number, results: Array}>}
 */
export async function getAttachments(params = {}, accessToken = null) {
  return apiGet(API_ENDPOINTS.attachments, accessToken, params)
}

/**
 * Получить вложение по ID
 * @param {number|string} attachmentId - ID вложения
 * @param {string} [accessToken] - Токен авторизации (опционально)
 * @returns {Promise<Object>}
 */
export async function getAttachment(attachmentId, accessToken = null) {
  return apiGet(API_ENDPOINTS.attachmentDetail(attachmentId), accessToken)
}

