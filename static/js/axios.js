axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';


export default function sendRequest(url, method, context) {
    try {
        let result = axios({
            method: method,
            url: url,
            data: context,
            query: context,
            withCredentials: true,
            credentials: 'include',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            },
            timeout: 10000,
            body: {}
        });
        console.log('axios request success: ', result);
        return result;
    } catch (error) {
        console.log('error: ', error)
    }
}
