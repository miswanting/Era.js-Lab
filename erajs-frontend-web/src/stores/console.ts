export default {
  namespaced: true,
  mutations: {
    toggle(state: any) {
      if ((globalThis as any).router.currentRoute.value.path === '/console') {
        (globalThis as any).router.back()
      } else {
        (globalThis as any).router.push('/console')
      }
    }
  }
}