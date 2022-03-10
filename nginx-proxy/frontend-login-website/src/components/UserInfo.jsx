import { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import { useNavigate } from "react-router";
import { get_user_info, user_logout } from "../api";
import LogoutBtn from "./LogoutBtn";

export default function UserInfo() {
    const [userEmail, setUserEmail] = useState("");
    const [userNickname, setUserNickname] = useState("");
    const [userBirthday, setUserBirthday] = useState("");
    const navigate = useNavigate();
    useEffect(() => {
        get_user_info()
            .then(res => res.data)
            .then(res => {
                setUserEmail(res.user_email)
                setUserNickname(res.user_nickname)
                setUserBirthday(res.user_birthday)
            }).catch(e => {
                navigate("/login?next=/user")
            });
    }, []);
    return (
        <div className="flex flex-col items-center">
            <div className="flex flex-col py-2 px-4 mb-6 rounded-lg border-2 border-blue-800 text-blue-800">
                <div className="mt-2 mb-1">Your Email </div>
                <div className="mb-4 w-60 font-medium" >{userEmail || <div className="text-gray-400">None</div>}</div>
                <div className="mb-1">Nickname</div>
                <div className="mb-4 w-60 font-medium" >{userNickname || <div className="text-gray-400">None</div>}</div>
                <div className="mb-1">Birthday</div>
                <div className="mb-4 w-60 font-medium" >{userBirthday || <div className="text-gray-400">None</div>}</div>
                <div className="flex justify-center">
                    <NavLink to="/user/edit" className="mx-2 cursor-pointer text-blue-900 font-bold"> Edit </NavLink>
                </div>
            </div>
            <LogoutBtn />
        </div>
    );
}