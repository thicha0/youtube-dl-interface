import axios from 'axios'

const instance = axios.create({
    baseURL: process.env.VUE_APP_API_URL,
    withCredentials: true,
})

//Change responseType to application/json in case of error
instance.interceptors.response.use(
    response => { return response; },
    error => {
        if (
            error.request.responseType === 'blob' &&
            error.response.data instanceof Blob
        )
        {
            return new Promise((resolve, reject) => {
                let reader = new FileReader()
                reader.onload = () => {
                    error.response.data = JSON.parse(reader.result)
                    resolve(Promise.reject(error))
                }

                reader.onerror = () => {
                    reject(error)
                }

                reader.readAsText(error.response.data)
            })
        }

        return Promise.reject(error)
    }
)

export default instance
