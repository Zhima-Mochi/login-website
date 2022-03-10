import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { get_user_info } from "../api";
import * as actions from '../actions';

export default function LoginStatus() {
    const dispatch = useDispatch();
    const userName = useSelector(state => state.userNameReducer);
    useEffect(() => {
        if (userName === "") {
            get_user_info().then(res => {
                const user_info = res.data;
                const user_name = user_info.user_nickname || user_info.user_email;
                dispatch(actions.get_user_name(user_name));
            }).catch(e => null);
        }
    }, [userName, dispatch]);
    if (userName === "") {
        return (
            <div className="flex text-white">
                <NavLink to="/login" className="mr-2">Login</NavLink>
                <NavLink to="/register" className="mr-2">Register</NavLink>
            </div>
        );
    } else {
        return (
            <div className="flex text-white">
                <NavLink to="/user" className="">{userName}</NavLink>
            </div>
        );
    }
}