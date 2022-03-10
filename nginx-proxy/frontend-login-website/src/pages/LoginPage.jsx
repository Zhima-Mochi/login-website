import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router";
import { get_login_status } from "../api";
import Header from "../components/Header";
import LoginForm from "../components/LoginForm";
import RegisterBtn from "../components/RegisterBtn";
import * as actions from '../actions';

export default function LoginPage() {
    const navigate = useNavigate();
    const dispatch=useDispatch();
    async function loginStatus() {
        return get_login_status().then(() => {
            navigate('/');
        }).catch(e => {
            dispatch(actions.remove_user_name());
        });
    }
    useEffect(() => {
        loginStatus();
    }, []);
    return (
        <div className="bg-blue-900">
            <div className="flex flex-col min-h-screen bg-opacity-30 bg-black">
                <Header />
                <div className="mx-auto my-20 flex flex-col items-center">
                    <div className="mb-4">
                        <LoginForm />
                    </div>
                    <div className="">
                        <RegisterBtn />
                    </div>
                </div>
            </div>
        </div>
    );
}