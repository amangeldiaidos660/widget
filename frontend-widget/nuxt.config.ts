// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  ssr: false,
  experimental: {
    payloadExtraction: false
  },
  devtools: { enabled: true },
  build: {
    // Настройка для сборки UMD
    outDir: 'dist',
    rollupOptions: {
      output: {
        format: 'umd',
        entryFileNames: 'widget.umd.js',
        name: 'Widget',
        exports: 'default',
      }
    }
  }
})
