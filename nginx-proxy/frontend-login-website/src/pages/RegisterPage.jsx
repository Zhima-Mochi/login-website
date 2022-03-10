import { useEffect } from "react";
import { useNavigate } from "react-router";
import { get_login_status } from "../api";
import Header from "../components/Header";
import RegisterForm from "../components/RegisterForm";
import * as actions from '../actions';
import { useDispatch } from "react-redux";

export default function RegisterPage() {
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
                <div className="mx-auto my-20">
                    <RegisterForm />
                </div>
            </div>
        </div>
    );
}