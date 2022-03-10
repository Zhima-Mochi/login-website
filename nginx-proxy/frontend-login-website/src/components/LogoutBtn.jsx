import { useDispatch } from "react-redux";
import { useNavigate } from "react-router";
import { user_logout } from "../api";
import * as actions from '../actions';

export default function LogoutBtn() {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    function logoutProcess() {
        user_logout()
            .then(() => {
                dispatch(actions.remove_user_name());
                navigate("/");
            })
            .catch(e => {
                navigate("/login?next=/user")
            });
    }
    return (<button onClick={() => logoutProcess()} className=" bg-red-400 text-white font-semibold rounded-lg w-32 border-2 border-white py-1" >Logout</button>);
}