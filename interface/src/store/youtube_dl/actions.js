import api from '@/service/api'
import { Message } from 'element-ui'

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
        link.setAttribute(
            'download',
            decodeURIComponent(escape(filename))
        );
        document.body.appendChild(link);
        link.click();
        commit('downloadSuccess')
        Message.success('Download completed !')
    }).catch((error) => {
        let errorMessage = 'An error has occurred.'
        if (error.response.status === 400) {
            commit('downloadError', error.response.data.error)
        }
        else if (error.response.status === 500) {
            errorMessage = error.response.data.error
            commit('downloadError', '')
        }
        Message.error(errorMessage)
    });
}

export default {
    downloadUrl,
}
