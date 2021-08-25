export default {
  namespaced: true,
  state: () => ({
    inited: false
  }),
  mutations: {
    set(state: any, value: boolean) {
      state.is = value
    }
  },
  actions: {
    init({ state }: any) {
      window.ws = new WebSocket(`ws://${window.location.host}/ws`);
      window.ws.addEventListener("open", () => {
        state.inited = true
        window.ws.addEventListener("message", (e) => {
          window.ws.send(e.data)
          console.log(e.data);
        });
        window.ws.send("connect")
      });
    },
    send(state: any, value: string) {
      if (state.inited) { window.ws.send(value) }
    }
  }
}