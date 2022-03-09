export class RegisterContent {
    constructor(user_email, user_password) {
        this.user_email = user_email;
        this.user_password = user_password;
    }
}

export class Oauth2Login {
    constructor(username, password, grant_type = "", scope = "", client_id = "", client_secret = "") {
        this.username = username;
        this.password = password;
        this.grant_type = grant_type;
        this.scope = scope;
        this.client_id = client_id;
        this.client_secret = client_secret;
    }
}