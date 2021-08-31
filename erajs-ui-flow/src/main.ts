import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'
import store from './stores/store'
import { } from 'spancharm-vue'
export default class UIManager {
  app: any
  store: any
  constructor() {
    this.app = createApp(App)
    // this.app.component('AppApp', App)
    // this.store = createStore({
    //   modules: { store }
    // })
    // this.app.use(this.store)
  }
  mount(el: any) {
    this.app.mount(el)
    // this.app.test()
  }
  push(data: any) {
    console.log(this.app);

  }
}
const um = new UIManager()
um.mount('body')
um.push({ type: 'text', data: { value: 'test' } })