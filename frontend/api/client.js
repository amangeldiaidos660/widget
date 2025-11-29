import { API_ENDPOINTS, BACKEND_BASE_URL } from './backendEndpoints.js'

/**
 * Базовый клиент для работы с API
 * Обеспечивает единообразную работу с бэкендом
 */

/**
 * Выполняет запрос к API с автоматической обработкой ошибок
 * @param {string} url - URL эндпоинта
 * @param {Object} options - Опции fetch (method, headers, body и т.д.)
 * @param {string} accessToken - Опциональный токен для авторизации
 * @returns {Promise<any>}
 */
export async function apiRequest(url, options = {}, accessToken = null) {
  const headers = {
    'Content-Type': 'application/json',
    ...options.headers,
  }

  if (accessToken) {
    headers['Authorization'] = `Bearer ${accessToken}`
  }

  const res = await fetch(url, {
    ...options,
    headers,
  })

  if (!res.ok) {
    const error = await res.json().catch(() => ({ 
      detail: `HTTP ${res.status}: ${res.statusText}` 
    }))
    throw new Error(error.detail || error.message || 'Ошибка запроса к API')
  }

  // Если ответ пустой (204 No Content), возвращаем null
  if (res.status === 204) {
    return null
  }

  return await res.json()
}

/**
 * GET запрос
 */
export async function apiGet(endpoint, accessToken = null, params = {}) {
  const url = new URL(endpoint, BACKEND_BASE_URL)
  Object.keys(params).forEach(key => {
    if (params[key] !== null && params[key] !== undefined) {
      url.searchParams.append(key, params[key])
    }
  })

  return apiRequest(url.toString(), {
    method: 'GET',
  }, accessToken)
}

/**
 * POST запрос
 */
export async function apiPost(endpoint, data, accessToken = null) {
  return apiRequest(endpoint, {
    method: 'POST',
    body: JSON.stringify(data),
  }, accessToken)
}

/**
 * PATCH запрос
 */
export async function apiPatch(endpoint, data, accessToken = null) {
  return apiRequest(endpoint, {
    method: 'PATCH',
    body: JSON.stringify(data),
  }, accessToken)
}

/**
 * PUT запрос
 */
export async function apiPut(endpoint, data, accessToken = null) {
  return apiRequest(endpoint, {
    method: 'PUT',
    body: JSON.stringify(data),
  }, accessToken)
}

/**
 * DELETE запрос
 */
export async function apiDelete(endpoint, accessToken = null) {
  return apiRequest(endpoint, {
    method: 'DELETE',
  }, accessToken)
}

