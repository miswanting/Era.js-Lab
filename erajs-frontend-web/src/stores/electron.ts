export default {
  namespaced: true,
  state: () => ({
    is: false
  }),
  mutations: {
    set(state: any, value: boolean) {
      state.is = value
    }
  }
}