import { NavLink } from "react-router-dom";

export default function LoginStatus() {
    return (
        <div className="flex text-white">
            <NavLink to="/login" className="mr-2">Login</NavLink>
            <NavLink to="/register" className="mr-2">Register</NavLink>
        </div>
    );
}