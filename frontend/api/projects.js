import { API_ENDPOINTS } from './backendEndpoints.js'
import { apiGet, apiPost } from './client.js'

/**
 * Модуль для работы с проектами
 */

/**
 * Получить список проектов (только активных)
 * @param {Object} params - Параметры (page, limit и т.д.)
 * @param {string} [accessToken] - Токен авторизации (опционально, т.к. read-only)
 * @returns {Promise<{count: number, results: Array}>}
 */
export async function getProjects(params = {}, accessToken = null) {
  return apiGet(API_ENDPOINTS.projects, accessToken, params)
}

/**
 * Получить проект по slug
 * @param {string} slug - Slug проекта
 * @param {string} [accessToken] - Токен авторизации (опционально)
 * @returns {Promise<Object>}
 */
export async function getProjectBySlug(slug, accessToken = null) {
  return apiGet(API_ENDPOINTS.projectDetail(slug), accessToken)
}

/**
 * Создать новый проект
 * @param {Object} data - { name, slug, is_active }
 * @param {string} [accessToken]
 * @returns {Promise<Object>}
 */
export async function createProject(data, accessToken = null) {
  return apiPost(API_ENDPOINTS.projects, data, accessToken)
}

