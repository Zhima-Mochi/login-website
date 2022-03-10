export const GET_USER_NAME = 'GET_USER_NAME';
export const REMOVE_USER_NAME = 'REMOVE_USER_NAME';

export const get_user_name = (user_name) => ({
    type: GET_USER_NAME,
    payload: user_name
});

export const remove_user_name = () => ({
    type: REMOVE_USER_NAME
});