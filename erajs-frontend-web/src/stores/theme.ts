export default {
  namespaced: true,
  state: () => ({
    dark: false
  }),
  mutations: {
    setIfDark(state: any, value: any) {
      state.dark = value
      if (state.dark) {
        document.documentElement.classList.add('dark')
      } else {
        document.documentElement.classList.remove('dark')
      }
    },
    toggleTheme(state: any) {
      state.dark = !state.dark
      if (state.dark) {
        document.documentElement.classList.add('dark')
      } else {
        document.documentElement.classList.remove('dark')
      }
    }
  }
}