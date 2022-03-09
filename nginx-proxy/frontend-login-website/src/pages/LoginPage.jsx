import Header from "../components/Header";
import LoginForm from "../components/LoginForm";

export default function LoginPage() {
    return (
        <div className="bg-blue-900">
            <div className="flex flex-col min-h-screen bg-opacity-30 bg-black">
                <Header />
                <div className="mx-auto my-20">
                    <LoginForm />
                </div>
            </div>
        </div>
    );
}