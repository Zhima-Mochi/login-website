import { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import { get_user_info } from "../api";

export default function LoginStatus() {
    const [isLogin, setIsLogin] = useState(false);
    const [userName, setUserName] = useState("");

    useEffect(() => {
        let saved = sessionStorage.getItem("user_name");
        if (!saved) {
            get_user_info().then(res => {
                const user_info = res.data;
                const user_name = user_info.user_nickname || user_info.user_email;
                sessionStorage.setItem("user_name", user_name);
                setUserName(user_name);
                console.log(userName);
                setIsLogin(true);
            });
        } else {
            const content = saved;
            setUserName(content);
            setIsLogin(true);
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
                <NavLink to="/user" className="">{userName}</NavLink>
            </div>
        );
    }
}