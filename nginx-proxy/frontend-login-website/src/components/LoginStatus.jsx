import { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import { get_login_status, get_user_info } from "../api";

export default function LoginStatus() {
    const [isLogin, setIsLogin] = useState(false);
    const [userInfo, setUserInfo] = useState({});

    async function loginStatus() {
        return get_login_status().then(() => {
            setIsLogin(true);
        }).catch(e => e);
    }
    useEffect(() => {
        loginStatus();
    }, []);

    useEffect(() => {
        if (!isLogin) {
            localStorage.removeItem("userInfo");
            return;
        }
        const saved = localStorage.getItem("userInfo");

        if (!saved) {
            get_user_info().then(res => {
                localStorage.setItem("userInfo", JSON.stringify(res.data));
                setUserInfo(res.data);
            });
        } else {
            const content = JSON.parse(saved);
            setUserInfo(content);
        }
    }, [isLogin]);
    if (!isLogin) {
        return (
            <div className="flex text-white">
                <NavLink to="/login" className="mr-2">Login</NavLink>
                <NavLink to="/register" className="mr-2">Register</NavLink>
            </div>
        );
    } else {
        return (
            <div className="flex text-white">
                <div className="">{userInfo.user_nickname || userInfo.user_email}</div>
            </div>
        );
    }
}