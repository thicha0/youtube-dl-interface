import api from '@/service/api'

export const downloadUrl = async (
    { commit },
    { url, format }
) => {
    commit('downloadLoading')

    api({
        method: 'post',
        url: '/youtube_dl/q',
        data: {
            "url": url,
            "format": format,
        },
        responseType: 'blob'
    }).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        const filename = response.headers['x-filename']
        link.setAttribute('download', filename);
        document.body.appendChild(link);
        link.click();
        commit('downloadSuccess', response.data.data)
    })
}

export default {
    downloadUrl,
}
