import * as actions from '../actions';
import {
    combineReducers
} from 'redux';

const userNameReducer = (state = "", action) => {
    switch (action.type) {
        case actions.GET_USER_NAME:
            return action.payload;
        case actions.REMOVE_USER_NAME:
            return "";
        default:
            return "";
    }
}

const rootReducer = combineReducers({
    userNameReducer: userNameReducer
});

export default rootReducer;