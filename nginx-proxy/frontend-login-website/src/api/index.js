import axios from "axios";
import qs from 'qs'

axios.defaults.withCredentials = true;

const api_url = new URL("http://localhost:8080/")
const api_base_path = ""

function get_api_url(api_url) {
    return process.env.REACT_APP_API+api_url.pathname;
}

function get_csrf_token() {
    let csrftoken_cookie = document.cookie.split(';').find((cookie) => cookie.trim().startsWith('csrftoken='));
    if (csrftoken_cookie) {
        csrftoken_cookie = csrftoken_cookie.trim().split('=')[1];
    }
    return csrftoken_cookie;
}

export async function submit_register(content) {
    api_url.pathname = api_base_path;
    api_url.pathname += "auth/register";
    const data = {
        ...content
    };
    return axios({
        method: 'post',
        url: get_api_url(api_url),
        data: data,
        headers: {
            'Content-Type': 'application/json'
        }
    });
}

export async function submit_login(content) {
    api_url.pathname = api_base_path;
    api_url.pathname += "auth/token";
    const data = {
        ...content
    };
    return axios({
        method: 'post',
        url: get_api_url(api_url),
        data: qs.stringify(data),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'accept': 'application/json'
        }
    });
}

export async function get_login_status() {
    api_url.pathname = api_base_path;
    api_url.pathname += "auth/login_status";
    return axios.get(get_api_url(api_url));
}

export async function get_user_info() {
    api_url.pathname = api_base_path;
    api_url.pathname += "users/info";
    return axios.get(get_api_url(api_url));
}

export async function user_logout() {
    api_url.pathname = api_base_path;
    api_url.pathname += "auth/logout";
    return axios.get(get_api_url(api_url), {
        headers: {
            'x-csrftoken': get_csrf_token()
        }
    });
}

export async function put_user_info(content) {
    api_url.pathname = api_base_path;
    api_url.pathname += "users/info";
    const data = {
        ...content
    };
    return axios.put(get_api_url(api_url), data);
}