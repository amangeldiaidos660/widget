import { API_ENDPOINTS } from './backendEndpoints.js'
import { apiGet, apiPost, apiPatch, apiDelete } from './client.js'

/**
 * Модуль для работы с заявками (tickets)
 */

/**
 * Получить список заявок
 * @param {Object} params - Параметры фильтрации (project__slug, status, assigned_to, search, page и т.д.)
 * @param {string} accessToken - Токен авторизации
 * @returns {Promise<{count: number, results: Array}>}
 */
export async function getTickets(params = {}, accessToken = null) {
  return apiGet(API_ENDPOINTS.tickets, accessToken, params)
}

/**
 * Получить заявку по ID
 * @param {number|string} ticketId - ID заявки
 * @param {string} accessToken - Токен авторизации
 * @returns {Promise<Object>}
 */
export async function getTicket(ticketId, accessToken = null) {
  return apiGet(API_ENDPOINTS.ticketDetail(ticketId), accessToken)
}

/**
 * Создать новую заявку (доступно анониму)
 * @param {Object} ticketData - Данные заявки
 * @param {string} ticketData.project_slug - Slug проекта
 * @param {string} ticketData.author_name - Имя автора
 * @param {string} ticketData.author_email - Email автора
 * @param {string} ticketData.description - Описание
 * @param {string} [ticketData.page_url] - URL страницы
 * @param {string} [ticketData.user_agent] - User Agent
 * @param {string} [ticketData.screen_resolution] - Разрешение экрана
 * @returns {Promise<Object>}
 */
export async function createTicket(ticketData) {
  return apiPost(API_ENDPOINTS.tickets, ticketData)
}

/**
 * Обновить заявку (частичное обновление, только status и assigned_to)
 * @param {number|string} ticketId - ID заявки
 * @param {Object} updates - Обновления ({status?: string, assigned_to?: number})
 * @param {string} accessToken - Токен авторизации
 * @returns {Promise<Object>}
 */
export async function updateTicket(ticketId, updates, accessToken) {
  return apiPatch(API_ENDPOINTS.ticketDetail(ticketId), updates, accessToken)
}

/**
 * Удалить заявку
 * @param {number|string} ticketId - ID заявки
 * @param {string} accessToken - Токен авторизации
 * @returns {Promise<void>}
 */
export async function deleteTicket(ticketId, accessToken) {
  return apiDelete(API_ENDPOINTS.ticketDetail(ticketId), accessToken)
}

