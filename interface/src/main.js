import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

// Element UI
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import locale from 'element-ui/lib/locale/lang/en'
Vue.use(ElementUI, { locale })

// Global style
import '@/assets/styles/style.scss'


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
