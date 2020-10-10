export default {
    downloadLoading(state) {
        state.downloadLoading = true
        state.downloadError = null
    },

    downloadSuccess(state) {
        state.downloadLoading = false
        state.downloadError = null
    },

    downloadError(state, error) {
        state.downloadLoading = false
        state.downloadError = error
    }
}