import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';

const version = '1.0.0';
export default defineConfig({
  plugins: [vue()],
  build: {
    lib: {
      entry: path.resolve(__dirname, 'main.js'),
      name: 'Widget',
      fileName: () => `widget.umd.v${version}.js`,
      formats: ['umd'],
    },
    rollupOptions: {
      external: ['vue', 'bootstrap', '@popperjs/core'],
      output: {
        globals: {
          vue: 'Vue',
          bootstrap: 'bootstrap',
          '@popperjs/core': 'Popper',
        },
      },
    },
    outDir: '../public',
    emptyOutDir: false,
  },
});
