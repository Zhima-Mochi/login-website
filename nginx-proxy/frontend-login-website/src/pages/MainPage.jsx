import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import Header from "../components/Header";

function Message() {
    const userName = useSelector(state => state.userNameReducer);
    if (userName !== "") {
        return (
            <div className="flex flex-col text-center">
                <div className="mb-4">Welcome to Main Page!</div>
                <div className="mb-4">You can check or edit your <NavLink to='/user' className="text-blue-500 underline">information</NavLink> now!</div>
            </div>
        );
    } else {
        return <div className="mb-4">Please <NavLink to='/login' className="text-blue-500 underline">login</NavLink> or <NavLink to='/register' className="text-red-300 underline">register</NavLink> first.</div>;
    }
}

export default function MainPage() {
    return (
        <div className="flex flex-col  min-h-screen bg-blue-50">
            <Header showStatus={true} />
            <div className="mt-40 flex flex-col items-center font-bold text-blue-800">
                <Message />
            </div>
        </div>
    );
}