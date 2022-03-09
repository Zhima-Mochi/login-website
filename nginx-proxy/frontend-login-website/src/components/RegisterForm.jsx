import { useState } from "react";
import { useNavigate } from "react-router";
import { submit_register } from "../api";
import { RegisterContent } from "../constants";

export default function RegisterForm() {
    const [userEmail, setUserEmail] = useState("");
    const [password, setPassword] = useState("");
    const [password2, setPassword2] = useState("");
    const [warning, setWarning] = useState("");
    const emailCheck = new RegExp(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
    const navigate = useNavigate();
    function eraseInput() {
        setWarning("");
        setUserEmail("");
        setPassword("");
        setPassword2("");
    }
    function submitProcess() {
        setWarning("");
        if (!emailCheck.test(userEmail)) {
            setWarning("* email is not valid!");
        } else if (password !== password2) {
            setWarning("* two passwords are not same!");
        } else {
            submit_register(new RegisterContent(userEmail, password))
                .then(() => navigate('/login'))
                .catch(e => {
                    if (e.response) {
                        setWarning("* " + e.response.data.detail);
                    }
                });
        }
    }
    return (
        <div className="">
            <div className="text-center text-blue-200 text-xl mb-2">Register</div>
            <div className="flex flex-col py-2 px-4 rounded-lg border-2 border-blue-200 text-blue-200">
                <div className="my-2">Your Email </div>
                <input type="email" value={userEmail} onChange={(e) => setUserEmail(e.target.value)} className="my-2 rounded-sm bg-blue-100 text-black px-1 w-60" />
                <div className="my-2">Create a password</div>
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className="my-2 rounded-sm bg-blue-100 text-black px-1 w-60" />
                <div className="my-2">Confirm password</div>
                <input type="password" value={password2} onChange={(e) => setPassword2(e.target.value)} className="my-2 rounded-sm bg-blue-100 text-black px-1 w-60" />
                <div className="text-red-600">{warning} </div>
                <div className="flex justify-center">
                    <button onClick={() => eraseInput()} className="mx-2 cursor-pointer text-red-400"> Cancel </button>
                    <button onClick={() => submitProcess()} className="mx-2 cursor-pointer"> Submit </button>
                </div>
            </div>
        </div>
    );
}