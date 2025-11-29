export default defineNuxtPlugin(() => {
  // Bootstrap CSS и JS уже подключены через nuxt.config.ts в head
  // Этот плагин нужен для дополнительной инициализации, если потребуется
  if (process.client) {
    // Bootstrap JS загружается через CDN в head
    // Можно добавить дополнительную инициализацию здесь
  }
})

