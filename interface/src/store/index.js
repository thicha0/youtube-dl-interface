import Vue from 'vue'
import Vuex from 'vuex'
import youtube_dl from './youtube_dl'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    youtube_dl,
  },
})