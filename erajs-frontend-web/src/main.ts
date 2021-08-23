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
import MUD from './routes/MUD.vue'
import AVG from './routes/AVG.vue'

import theme from './stores/theme'
import console from './stores/console'
import locale from './stores/locale'
import electron from './stores/electron'
import ws from './stores/ws'

import isElectron from 'is-electron'

window.isElectron = isElectron()

window.app = createApp(App)

window.store = createStore({
  modules: {
    theme,
    console,
    locale,
    electron,
    ws
  }
})
window.app.use(window.store)

window.router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/idle', component: Idle },
    { path: '/console', component: Console },
    { path: '/mud', component: MUD },
    { path: '/avg', component: AVG }
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

// window.ws = new WebSocket("ws://localhost:8000/ws");
// window.ws.addEventListener("open", () => {
//   window.ws.addEventListener("message", (e) => {
//     console.log(e);
//   });
//   window.ws.send("test");
// });