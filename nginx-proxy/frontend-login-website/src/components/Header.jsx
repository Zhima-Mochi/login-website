import { NavLink } from "react-router-dom";
export default function Header({ showStatus = false }) {
    return (
        <div className="bg-blue-800 mb-2 lg:mb-4 shadow-md">
            <div className="wrap">
                <div className="flex items-center py-1 lg:py-2">
                    <NavLink to='/'>
                        <div className="text-white text-2xl">U-Page</div>
                    </NavLink>
                </div>
            </div>
        </div>
    );
}