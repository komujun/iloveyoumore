import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    req: {},
    res: {},
  },
  mutations: {
    setReq(state, req) {
      state.req = req;
    },
    setRes(state, res) {
      state.res = res;
    },
    clearReq(state) {
      state.req = {};
    },
    clearRes(state) {
      state.req = {};
    },
  },
});

export default store;
