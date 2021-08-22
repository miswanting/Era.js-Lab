export default {
  namespaced: true,
  mutations: {
    set(state: any, value: string) {
      (globalThis as any).i18n.global.locale = value
    },
    toggle(state: any) {
      if ((globalThis as any).i18n.global.locale === 'zh-CN') (globalThis as any).i18n.global.locale = 'en-US'
      else if ((globalThis as any).i18n.global.locale === 'en-US') (globalThis as any).i18n.global.locale = 'ja-JP'
      else (globalThis as any).i18n.global.locale = 'zh-CN'
    }
  }
}