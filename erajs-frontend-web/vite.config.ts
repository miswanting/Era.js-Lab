import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import WindiCSS from 'vite-plugin-windicss'
import yaml from '@rollup/plugin-yaml'

export default defineConfig({
  plugins: [vue(), WindiCSS(), yaml()],
  server: {
    port: 8080
  }
})
