import 'normalize.css'
import '@fortawesome/fontawesome-free/css/all.css'
import '@mdi/font/css/materialdesignicons.min.css'
import 'virtual:windi.css'

import en from './locales/en.yml'
import zh from './locales/zh.yml'

import { createApp } from 'vue'
import { createStore } from 'vuex'
import { createRouter, createWebHistory } from 'vue-router'
import { createI18n } from 'vue-i18n'
import App from './App.vue'
import Idle from './routes/Idle.vue'
const app = createApp(App)
const store = createStore({
  modules: {
    theme: {
      namespaced: true,
      state: () => ({
        light: true
      }),
      mutations: {
        setIfLight(state, value) {
          state.light = value
          if (state.light) {
            document.documentElement.classList.add('light')
          } else {
            document.documentElement.classList.add('dark')
          }
        },
        toggleTheme(state) {
          state.light = !state.light
          if (state.light) {
            document.documentElement.classList.add('light')
          } else {
            document.documentElement.classList.add('dark')
          }
        }
      }
    }
  }
})
app.use(store)
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Idle }
  ]
})
app.use(router)
const i18n = createI18n({
  locale: 'zh',
  fallbackLocale: 'en',
  messages: {
    en, zh
  }
})
app.use(i18n)
app.mount('body')
