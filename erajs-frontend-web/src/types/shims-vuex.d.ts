import { Store } from 'vuex';

declare module '@vue/runtime-core' {
    interface State {
        count: number
        theme: any
    }
    interface ComponentCustomProperties {
        $store: Store<State>;
    }
}