<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>Download Youtube Video</h1>
    <el-input placeholder="https://www.youtube.com/watch?v=1234567890a" v-model="link" />
    <el-button type="primary" @click="submit">Download <i class="el-icon-download el-icon-right"></i></el-button>
  </div>
</template>

<script>
import { Input, Button } from 'element-ui'
import Vue from 'vue'
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(Input)
Vue.use(Button)
export default {
  name: 'Home',
  data() {
    return {
      link: ''
    }
  },
  methods: {
    submit() {
      if(!this.link.startsWith('https://www.youtube.com/watch?v=')) {
        alert('NOPE')
        return
      }
      alert('ALL GOOD')
    }
  }
}
</script>
