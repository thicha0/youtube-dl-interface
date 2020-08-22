<template>
  <div class="home">
    <img class="logo" alt="logo" src="../assets/logo.png">
    <h1 class="title">Download Youtube Videos</h1>
    <el-input
            class="input"
            placeholder="https://www.youtube.com/watch?v=1234567890a"
            v-model="url"
            :error="downloadError"
    />

    <el-switch
        class="switch"
        v-model="format"
        active-text="Audio"
        active-value="audio"
        active-color="red"
        inactive-text="Video"
        inactive-value="video"
        inactive-color="red"
        font-size="50px"
    />

    <el-button
        v-loading="downloadLoading"
        class="button"
        @click="submit"
    >
      Download <i class="el-icon-download"></i>
    </el-button>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { Input, Button, Switch } from 'element-ui'
import Vue from 'vue'

Vue.use(Input)
Vue.use(Button)
Vue.use(Switch)
export default {
  name: 'Home',
  data() {
    return {
      url: '',
      format: 'video',
    }
  },
  computed: {
    ...mapState('youtube_dl', [
      'downloadLoading',
      'downloadSuccess',
      'downloadError'
    ])
  },
  methods: {
    ...mapActions('youtube_dl', ['downloadUrl']),
    submit() {
      if (this.downloadLoading) return
      this.downloadUrl({
        url: this.url,
        format: this.format,
      })
    }
  }
}
</script>
