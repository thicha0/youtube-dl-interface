<template>
  <div class="home">
    <h1 class="title">Download Youtube Video</h1>
    <el-input class="input" placeholder="https://www.youtube.com/watch?v=1234567890a" v-model="url" />
    <el-select v-model="format">
      <el-option
        v-for="item in formatOptions"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>

    <el-button
            v-loading="downloadLoading"
            plain class="button"
            type="primary"
            @click="submit"
    >
      Download <i class="el-icon-download el-icon-right"></i>
    </el-button>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { Input, Button } from 'element-ui'
import Vue from 'vue'

Vue.use(Input)
Vue.use(Button)
export default {
  name: 'Home',
  data() {
    return {
      url: '',
      format: 'video',
      formatOptions: [{
        value: 'video',
        label: 'Video'
      }, {
        value: 'audio',
        label: 'Audio'
      }],
    }
  },
  computed: {
    ...mapState('youtube_dl', [
      'download',
      'downloadLoading',
      'downloadSuccess',
      'downloadError'
    ])
  },
  methods: {
    ...mapActions('youtube_dl', ['downloadUrl']),
    submit() {
      // if(!this.url.startsWith('https://www.youtube.com/watch?v=')) {
      //   alert('NOPE')
      //   return
      // }
      this.downloadUrl({
        url: this.url,
        format: this.format,
      })
    }
  }
}
</script>

<style>
  .home {
    background-color: powderblue;
    justify-content: space-between;
    padding: 3%;
    text-align: center;
  }

  .title {
    font-family: "Segoe UI", sans-serif;
  }

  .input {
    margin: 1%;
    max-width: 50%;
  }

  .button {

  }
</style>
