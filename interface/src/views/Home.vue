<template>
  <div class="home">
    <img class="logo" alt="logo" src="../assets/logo.png">
    <h1 class="title">Download Youtube Videos</h1>
    <el-form>
      <el-form-item :error="downloadError">
        <el-input
          class="input"
          placeholder="https://www.youtube.com/watch?v=1234567890a"
          v-model="url"
        />
      </el-form-item>

      <el-form-item>
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
      </el-form-item>

      <el-button
        v-loading="downloadLoading"
        class="button"
        @click="submit"
      >
        Download <i class="el-icon-download"></i>
      </el-button>
    </el-form>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

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
