# API модули

Централизованная структура для работы с бэкенд API.

## Структура

```
api/
├── backendEndpoints.js  # Все эндпоинты в одном месте
├── client.js           # Базовый клиент для HTTP запросов
├── auth.js             # Модуль авторизации
├── health.js           # Проверка здоровья API
├── tickets.js          # Работа с заявками
├── projects.js         # Работа с проектами
├── comments.js         # Работа с комментариями
└── attachments.js      # Работа с вложениями
```

## Использование

### 1. Добавление нового эндпоинта

В `backendEndpoints.js`:
```javascript
export const API_ENDPOINTS = {
  // ... существующие эндпоинты
  newEndpoint: `${BACKEND_BASE_URL}/api/new-endpoint/`,
  newEndpointDetail: (id) => `${BACKEND_BASE_URL}/api/new-endpoint/${id}/`,
}
```

### 2. Создание модуля для работы с эндпоинтом

Создайте файл `api/newModule.js`:
```javascript
import { API_ENDPOINTS } from './backendEndpoints.js'
import { apiGet, apiPost } from './client.js'

export async function getItems(params = {}, accessToken = null) {
  return apiGet(API_ENDPOINTS.newEndpoint, accessToken, params)
}

export async function createItem(data, accessToken) {
  return apiPost(API_ENDPOINTS.newEndpoint, data, accessToken)
}
```

### 3. Использование в компонентах/stores

```javascript
import * as ticketsApi from '~/api/tickets.js'
import { useAuthStore } from '~/stores/auth.js'

const authStore = useAuthStore()

// Получить список заявок
const tickets = await ticketsApi.getTickets(
  { project__slug: 'test-app', status: 'NEW' },
  authStore.token
)

// Создать заявку (без токена, доступно анониму)
const newTicket = await ticketsApi.createTicket({
  project_slug: 'test-app',
  author_name: 'Иван',
  author_email: 'ivan@example.com',
  description: 'Описание проблемы'
})
```

## Базовый клиент (client.js)

Предоставляет унифицированные методы:
- `apiGet(url, accessToken, params)` - GET запрос
- `apiPost(url, data, accessToken)` - POST запрос
- `apiPatch(url, data, accessToken)` - PATCH запрос
- `apiPut(url, data, accessToken)` - PUT запрос
- `apiDelete(url, accessToken)` - DELETE запрос

Все методы автоматически:
- Добавляют заголовок `Authorization: Bearer {token}` если передан токен
- Обрабатывают ошибки
- Парсят JSON ответы

## Примеры

### Авторизация
```javascript
import * as authApi from '~/api/auth.js'

// Вход
const { access, refresh } = await authApi.login('username', 'password')

// Получить текущего пользователя
const user = await authApi.getCurrentUser(accessToken)

// Обновить токен
const { access } = await authApi.refreshToken(refreshToken)
```

### Работа с заявками
```javascript
import * as ticketsApi from '~/api/tickets.js'

// Список заявок с фильтрами
const tickets = await ticketsApi.getTickets({
  project__slug: 'test-app',
  status: 'NEW',
  search: 'ошибка',
  page: 1
}, accessToken)

// Создать заявку (без токена)
const ticket = await ticketsApi.createTicket({
  project_slug: 'test-app',
  author_name: 'Иван',
  author_email: 'ivan@example.com',
  description: 'Проблема с кнопкой'
})

// Обновить статус заявки
await ticketsApi.updateTicket(ticketId, {
  status: 'IN_PROGRESS',
  assigned_to: userId
}, accessToken)
```

### Работа с проектами
```javascript
import * as projectsApi from '~/api/projects.js'

// Список проектов
const projects = await projectsApi.getProjects()

// Проект по slug
const project = await projectsApi.getProjectBySlug('test-app')
```

