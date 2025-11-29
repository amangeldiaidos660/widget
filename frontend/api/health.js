import { API_ENDPOINTS } from './backendEndpoints.js'
import { apiGet } from './client.js'

/**
 * Проверка здоровья API
 * @returns {Promise<{status: string}>}
 */
export async function fetchHealth() {
  return apiGet(API_ENDPOINTS.health)
}
