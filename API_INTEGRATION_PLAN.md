# План интеграции API с базой данных

## Текущее состояние

### База данных
- **Местоположение**: `backend/db.sqlite3`
- **Настройка**: В `settings.py` настроена PostgreSQL (но используется SQLite в dev)
- **Модели**:
  - `Project` - проекты/приложения
  - `Ticket` - заявки/тикеты
  - `Comment` - комментарии
  - `Attachment` - вложения
  - `ResponsibleMapping` - связь проектов и ответственных

### Backend API (Django REST)
**Базовый URL**: `https://api.neurocity.app`

#### Endpoints:
- `GET /api/projects/` - список проектов
- `POST /api/projects/` - создать проект (admin)
- `GET /api/projects/{slug}/` - получить проект по slug

- `GET /api/tickets/` - список заявок (фильтры: project__slug, status, assigned_to, search)
- `POST /api/tickets/` - создать заявку (доступно анониму)
- `GET /api/tickets/{id}/` - получить заявку
- `PATCH /api/tickets/{id}/` - обновить заявку (status, assigned_to)

- `GET /api/comments/?ticket={id}` - комментарии к заявке
- `POST /api/comments/` - создать комментарий

- `POST /api/token/` - получить JWT токен
- `GET /api/user/` - текущий пользователь
- `GET /api/users/staff/` - список сотрудников

### Frontend API клиенты
Все готовы в `frontend/api/`:
- `auth.js` - авторизация
- `tickets.js` - работа с заявками ✅
- `projects.js` - работа с проектами ✅
- `users.js` - работа с пользователями
- `comments.js` - работа с комментариями

## Статус страниц

### ✅ Интегрировано
1. **index.vue** (Dashboard) - использует `getTickets()` API
2. **TicketDetail.vue** - использует `getTicket()` и `updateTicket()`
3. **login.vue** - использует auth API

### ⚠️ Требуют доработки

#### 1. **tickets.vue**
**Проблема**: Использует хардкод данных
**Решение**:
```javascript
// Добавить:
import { getTickets } from '~/api/tickets'
import { useAuthStore } from '~/stores/auth'

// Загрузка данных:
const fetchTickets = async () => {
  loading.value = true
  try {
    const data = await getTickets({
      status: filters.value.status,
      search: filters.value.search
    }, authStore.token)
    allTickets.value = data.results || []
  } catch (error) {
    console.error('Error:', error)
  } finally {
    loading.value = false
  }
}
```

#### 2. **ProjectsCreate.vue**
**Проблема**: Ошибки не переведены
**Статус**: API интеграция работает ✅
**Осталось**: Добавить обработку ошибок

#### 3. **reports.vue**
**Проблема**: Все данные хардкод
**Решение**: Нужно создать API endpoint для статистики или вычислять на фронте

#### 4. **status.vue**
**Проблема**: Данные хардкод
**Решение**: Интегрировать с `/api/health/`

#### 5. **profile.vue**
**Проблема**: Данные не сохраняются
**Решение**: 
- Использовать `/api/user/` для получения данных
- Создать endpoint для обновления профиля

## Необходимые изменения

### 1. Доработка backend

#### Добавить endpoint для статистики
```python
# feedback_app/views.py
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    """Статистика для дашборда"""
    tickets = Ticket.objects.all()
    
    # Фильтр по проекту если указан
    project_slug = request.query_params.get('project')
    if project_slug:
        tickets = tickets.filter(project__slug=project_slug)
    
    return Response({
        'total': tickets.count(),
        'new': tickets.filter(status='NEW').count(),
        'in_progress': tickets.filter(status='IN_PROGRESS').count(),
        'closed': tickets.filter(status='CLOSED').count(),
    })
```

#### Добавить endpoint для обновления профиля
```python
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_profile(request):
    """Обновление профиля пользователя"""
    user = request.user
    # Обновление полей
    return Response(UserSerializer(user).data)
```

### 2. Исправления во frontend

#### tickets.vue
- Убрать хардкод tickets
- Использовать API для загрузки
- Добавить пагинацию

#### reports.vue  
- Использовать реальные данные из API
- Или вычислять на основе tickets

#### profile.vue
- Загружать данные пользователя из API
- Сохранять изменения через API

### 3. Проверить docker-compose.yml

Убедиться что:
- Backend правильно подключен к БД
- CORS настроен
- Frontend может обращаться к backend

## Следующие шаги

1. ✅ index.vue - интегрирован с API
2. ⏳ tickets.vue - добавить загрузку из API
3. ⏳ Создать endpoint для статистики
4. ⏳ reports.vue - использовать API статистики
5. ⏳ profile.vue - интегрировать с user API
6. ⏳ Проверить все кнопки работают

## Проблемы для решения

1. **База данных**: Решить SQLite vs PostgreSQL (для dev можно SQLite)
2. **Приоритеты**: В модели Ticket нет поля priority (нужно добавить миграцию)
3. **Аутентификация**: Проверить что auth store правильно сохраняет токен
4. **CORS**: Проверить что фронт может обращаться к бэкенду
