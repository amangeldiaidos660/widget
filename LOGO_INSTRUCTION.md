# Инструкция по замене логотипа ARRFR

## Где находится логотип

Логотип расположен в **двух местах**:

### 1. В Layout (для всех страниц с сайдбаром)
**Файл:** `frontend/layouts/default.vue`
**Строки:** 10-18

```vue
<div class="h-10 w-10 rounded-lg bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center">
  <!-- Вставьте ваш логотип ARRFR здесь -->
  <!-- SVG placeholder - замените на ваш логотип -->
  <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
  </svg>
</div>
```

### 2. На странице логина
**Файл:** `frontend/pages/login.vue`
**Строки:** 6-12

```vue
<div class="inline-flex h-16 w-16 items-center justify-center rounded-2xl bg-white shadow-lg mb-4">
  <svg class="h-10 w-10 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
  </svg>
</div>
```

---

## Варианты замены

### Вариант 1: SVG логотип (рекомендуется)
Если у вас есть SVG файл логотипа:

```vue
<!-- В layout -->
<div class="h-10 w-10 rounded-lg flex items-center justify-center">
  <img src="/logo-arrfr.svg" alt="ARRFR Logo" class="h-8 w-8" />
</div>

<!-- На странице логина -->
<div class="inline-flex h-16 w-16 items-center justify-center rounded-2xl bg-white shadow-lg mb-4">
  <img src="/logo-arrfr.svg" alt="ARRFR Logo" class="h-12 w-12" />
</div>
```

Разместите файл `logo-arrfr.svg` в папке `frontend/public/`

---

### Вариант 2: PNG/JPG логотип
Если у вас есть PNG или JPG:

```vue
<!-- В layout -->
<div class="h-10 w-10 rounded-lg flex items-center justify-center overflow-hidden">
  <img src="/logo-arrfr.png" alt="ARRFR Logo" class="h-full w-full object-contain" />
</div>

<!-- На странице логина -->
<div class="inline-flex h-16 w-16 items-center justify-center rounded-2xl bg-white shadow-lg mb-4 overflow-hidden">
  <img src="/logo-arrfr.png" alt="ARRFR Logo" class="h-12 w-12 object-contain" />
</div>
```

Разместите файл `logo-arrfr.png` в папке `frontend/public/`

---

### Вариант 3: Inline SVG код
Если у вас есть SVG код логотипа, вставьте его напрямую:

```vue
<!-- В layout -->
<div class="h-10 w-10 rounded-lg flex items-center justify-center">
  <svg class="h-8 w-8" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <!-- Ваш SVG код здесь -->
    <circle cx="50" cy="50" r="40" fill="white"/>
    <!-- ... остальной код ... -->
  </svg>
</div>
```

---

### Вариант 4: Использовать текстовый логотип
Если логотипа нет, можно использовать стилизованный текст:

```vue
<!-- В layout -->
<div class="h-10 w-10 rounded-lg bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center">
  <span class="text-white font-bold text-xl">AF</span>
</div>

<!-- На странице логина -->
<div class="inline-flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-blue-500 to-blue-700 shadow-lg mb-4">
  <span class="text-white font-bold text-3xl">AF</span>
</div>
```

---

## Рекомендации

1. **Формат:** Используйте SVG для лучшего качества на всех экранах
2. **Размер файла:** Оптимизируйте изображение (< 50KB)
3. **Прозрачность:** Если используете PNG, убедитесь что фон прозрачный
4. **Цвета:** Адаптируйте цвета под темный фон (сайдбар) и светлый (логин)

---

## После замены

Перезапустите Docker контейнер:
```bash
docker compose restart frontend-portal
```

Или пересоберите:
```bash
docker compose down
docker compose up -d --build frontend-portal
```
