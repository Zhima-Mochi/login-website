import Header from "../components/Header";
import RegisterForm from "../components/RegisterForm";

export default function RegisterPage() {
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