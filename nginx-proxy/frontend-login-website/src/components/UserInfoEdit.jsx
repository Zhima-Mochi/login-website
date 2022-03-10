import { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import { useNavigate } from "react-router";
import { get_user_info } from "../api";

export default function UserInfoEdit() {
    const [userEmail, setUserEmail] = useState("");
    const [userNickname, setUserNickname] = useState("");
    const [userBirthday, setUserBirthday] = useState("");
    const navigate = useNavigate();
    useEffect(() => {
        get_user_info()
            .then(res => res.data)
            .then(res => {
                setUserEmail(res.user_email)
                setUserNickname(res.user_nickname || "")
                setUserBirthday(res.user_birthday || (new Date().toISOString()).split('T')[0])
            }).catch(e => {
                navigate("/login?next=/user/edit")
            });
    }, []);
    return (
        <div className="">
            <div className="flex flex-col py-2 px-4 rounded-lg border-2 border-blue-800 text-blue-800">
                <div className="mt-2 mb-1">Your Email </div>
                <div className="mb-4 w-60 font-medium" >{userEmail || <div className="text-gray-400">None</div>}</div>
                <div className="mb-1">Nickname</div>
                <input type="text" value={userNickname} onChange={(e) => setUserNickname(e.target.value)} className="my-2 rounded-sm bg-white text-black px-1 w-60" />
                <div className="mb-1">Birthday</div>
                <input type="date" value={userBirthday} onChange={(e) => setUserBirthday(e.target.value)} className="my-2 rounded-sm bg-white text-black px-1 w-60" />
                <div className="flex justify-center">
                    <button onClick={() => navigate('/user')} className="mx-2 cursor-pointer text-red-400 font-bold"> Cancel </button>
                    <button to="/user/edit" className="mx-2 cursor-pointer text-blue-900 font-bold"> Confirm </button>
                </div>
            </div>
        </div>
    );
}