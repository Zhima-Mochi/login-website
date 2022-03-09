import axios from "axios";
import qs from 'qs'

axios.defaults.withCredentials = true;

const api_url = new URL("http://localhost:8080/")
const api_base_path = ""

export async function submit_register(content) {
    api_url.pathname = api_base_path;
    api_url.pathname += "auth/register";
    const data = {
        ...content
    };
    return axios({
        method: 'post',
        url: api_url.href, //
        data: data,
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(res => {
        return res;
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
        url: api_url.href, //
        data: qs.stringify(data),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'accept': 'application/json'
        }
    }).then(res => {
        return res;
    });
}

export async function get_login_status() {
    api_url.pathname = api_base_path;
    api_url.pathname += "auth/login_status";
    return axios.get(api_url.href)
        .then(res => res);
}

export async function get_user_info() {
    api_url.pathname = api_base_path;
    api_url.pathname += "users/info";
    return axios.get(api_url.href).then(res => res);
}