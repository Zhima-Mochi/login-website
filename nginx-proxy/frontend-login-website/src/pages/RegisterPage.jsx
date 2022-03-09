import { useEffect } from "react";
import { useNavigate } from "react-router";
import { get_login_status } from "../api";
import Header from "../components/Header";
import RegisterForm from "../components/RegisterForm";

export default function RegisterPage() {
    const navigate = useNavigate();
    async function loginStatus() {
        return get_login_status().then(() => {
            navigate('/');
        }).catch(e => console.log(e));
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