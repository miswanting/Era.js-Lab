import 'normalize.css'
import '@fortawesome/fontawesome-free/css/all.css'
import './styles/index.styl'
import 'virtual:windi.css'
import 'virtual:windi-devtools'

import { createApp } from 'vue'
import { createStore } from 'vuex'
import { createRouter, createWebHistory } from 'vue-router'
import { createI18n } from 'vue-i18n'

import zh_CN from './locales/zh-CN.yml'
import en_US from './locales/en-US.yml'
import ja_JP from './locales/ja-JP.yml'

import App from './App.vue'
import Idle from './routes/Idle.vue'
import Console from './routes/Console.vue'
import AVGGame from './routes/AVGGame.vue'

import themeStore from './stores/theme'
import consoleStore from './stores/console'
import localeStore from './stores/locale'

import isElectron from 'is-electron'

window.isElectron = isElectron()

window.app = createApp(App)

window.store = createStore({
  modules: {
    theme: themeStore,
    console: consoleStore,
    locale: localeStore
  }
})
window.app.use(window.store)

window.router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/idle', component: Idle },
    { path: '/console', component: Console },
    { path: '/AVG', component: AVGGame }
  ]
})
window.app.use(window.router)

window.i18n = createI18n({
  locale: 'zh-CN',
  fallbackLocale: 'en-US',
  globalInjection: true,
  messages: {
    'zh-CN': zh_CN,
    'en-US': en_US,
    'ja-JP': ja_JP,
  }
})
window.app.use(window.i18n)

window.app.mount('body')
