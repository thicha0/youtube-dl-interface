import api from '@/service/api'

export const downloadUrl = async (
    { commit },
    { url, format }
) => {
    commit('downloadLoading')
    try {
        const response = await api.post(
            '/youtube_dl/q',
            {
                "url": url,
                "format": format,
            }
        )
        commit('downloadSuccess', response.data.data)
    } catch (e) {
        commit('downloadError', e.response.data)
    }
}

export default {
    downloadUrl,
}
