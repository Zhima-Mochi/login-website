import { useNavigate } from "react-router";

export default function RegisterBtn(){
    const navigate=useNavigate();
    return (
    <button onClick={() => navigate('/register')} className="  text-white font-semibold rounded-lg w-32 py-1 underline" >
        Register
    </button>);
}