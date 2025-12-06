// backendEndpoints.js
// Главная точка входа для всех API-эндпоинтов и базового URL backend

// Определяем backend URL в зависимости от окружения
const getBackendURL = () => {
  // В браузере проверяем hostname
  if (typeof window !== 'undefined') {
    const hostname = window.location.hostname
    if (hostname === 'localhost' || hostname === '127.0.0.1') {
      return 'http://localhost:8001'
    }
  }
  return 'https://api.neurocity.app'
}

export const BACKEND_BASE_URL = getBackendURL()

export const API_ENDPOINTS = {
  // Health check
  health: `${BACKEND_BASE_URL}/api/health/`,
  
  // Authentication
  token: `${BACKEND_BASE_URL}/api/token/`,
  tokenRefresh: `${BACKEND_BASE_URL}/api/token/refresh/`,
  currentUser: `${BACKEND_BASE_URL}/api/user/`,
  staffUsers: `${BACKEND_BASE_URL}/api/users/staff/`,
  
  // Projects
  projects: `${BACKEND_BASE_URL}/api/projects/`,
  projectDetail: (id) => `${BACKEND_BASE_URL}/api/projects/${id}/`,
  
  // Tickets
  tickets: `${BACKEND_BASE_URL}/api/tickets/`,
  ticketDetail: (id) => `${BACKEND_BASE_URL}/api/tickets/${id}/`,
  
  // Comments
  comments: `${BACKEND_BASE_URL}/api/comments/`,
  commentDetail: (id) => `${BACKEND_BASE_URL}/api/comments/${id}/`,
  
  // Attachments
  attachments: `${BACKEND_BASE_URL}/api/attachments/`,
  attachmentDetail: (id) => `${BACKEND_BASE_URL}/api/attachments/${id}/`,
}
