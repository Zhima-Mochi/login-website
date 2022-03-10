import { useState } from "react";
import { useNavigate } from "react-router";
import { useSearchParams } from "react-router-dom";
import { submit_login } from "../api";
import { Oauth2Login } from "../constants";

export default function LoginForm() {
    const [userEmail, setUserEmail] = useState("");
    const [password, setPassword] = useState("");
    const [warning, setWarning] = useState("");
    const emailCheck = new RegExp(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
    const navigate = useNavigate();
    const [searchParams] = useSearchParams();
    
    function eraseInput() {
        setWarning("");
        setUserEmail("");
        setPassword("");
    }
    function submitProcess() {
        setWarning("");
        if (!emailCheck.test(userEmail)) {
            setWarning("* email is not valid!");
        } else {
            submit_login(new Oauth2Login(userEmail, password))
                .then(() => {
                    if (searchParams.get('next')) {
                        navigate(searchParams.get('next'));
                    } else {
                        navigate('/');
                    }
                })
                .catch(e => {
                    if (e.response) {
                        setWarning("* " + e.response.data.detail);
                    }
                });
        }
    }
    return (
        <div className="">
            <div className="text-center text-blue-200 text-xl mb-2">Login</div>
            <div className="flex flex-col py-2 px-4 rounded-lg border-2 border-blue-200 text-blue-200">
                <div className="my-2">Your Email </div>
                <input type="email" value={userEmail} onChange={(e) => setUserEmail(e.target.value)} className="my-2 rounded-sm bg-blue-100 text-black px-1 w-60" />
                <div className="my-2">Password</div>
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className="my-2 rounded-sm bg-blue-100 text-black px-1 w-60" />
                <div className="text-red-600">{warning} </div>
                <div className="flex justify-center">
                    <button onClick={() => eraseInput()} className="mx-2 cursor-pointer text-red-400"> Cancel </button>
                    <button onClick={() => submitProcess()} className="mx-2 cursor-pointer"> Submit </button>
                </div>
            </div>
        </div>
    );
}