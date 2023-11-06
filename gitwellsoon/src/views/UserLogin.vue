<template>
    <div class="container">
        <div class="row justify-content-center mt-5 mb-5">
            <div class="col-6">
                <div class="checkout_details_area mt-50 clearfix">
                    
                    <div v-if="defaultView == 'createAccount'">
                        
                        <div class="cart-page-heading text-center">
                            <h3>Create an account</h3>
                            <p>Please create an account and verify your email address before proceeding to place order!</p>
                        </div>
    
                        <div class="row">
                            <div class="col-12 mb-3">
                                <label for="username">Username<span>*</span></label>
                                <input type="text" v-model="userName" class="form-control" id="username">
                            </div>
                            <div class="col-12 mb-3">
                                <label for="email">Email<span>*</span></label>
                                <input type="text" v-model="userEmail" class="form-control" id="email">
                            </div>
                            <div class="col-12 mb-4">
                                <label for="Password">Password<span>*</span></label>
                                <input type="password" v-model="userPassword" class="form-control" id="Password">
                            </div>
                            <div class="col-12 text-center">
                                <button class="btn btn-success" @click="createAccount()">Create Account</button>
                            </div>
                        </div>
                        <div  class="text-center">
                            <h3>Or If you already have an account</h3>
                            <button class="btn btn-success" @click="ChangeView()">Login</button>
                        </div>
                    </div>
                    <div v-else>
                        <div class="cart-page-heading text-center">
                            <h3>Login</h3>
                            <p>Please login before proceeding to place order!</p>
                        </div>
                        <div class="row">
                            <div class="col-12 mb-3">
                                <label for="email">Email<span>*</span></label>
                                <input type="text" v-model="userEmail" class="form-control" id="email">
                            </div>
                            <div class="col-12 mb-4">
                                <label for="Password">Password<span>*</span></label>
                                <input type="password" v-model="userPassword" class="form-control" id="Password">
                            </div>
                            <div class="col-12 text-center">
                                <button class="btn btn-success" @click="login()">Login</button>
                            </div>
                        </div>
                        <div class="text-center">
                            <h3>Or If you don't have an account</h3>
                            <button class="btn btn-success" @click="ChangeView()">Create Account</button>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex";

export default {
    name: "UserLoginPage",
    components: {
    },
    data(){
        return {
            emailTriggerSuccessCode: 0,
            userEmail: "",
            userPassword: "",
            userName: "",
            defaultView: "createAccount"
        }
    },
    methods: {
        ...mapActions(['createUserAccount', 'logIn']),
        ChangeView() {
            if (this.defaultView == "createAccount") {
                this.defaultView = "Login"
            } else {
                this.defaultView = "createAccount"
            }
        },
        async createAccount() {
            //create account
            let res = await this.createUserAccount({'username': this.userName, 'email': this.userEmail, 'password': this.userPassword});
            console.log(res);
            try {
                if (res.code == 200) {
                    var bodyJSON = JSON.stringify({
                        email: this.userEmail
                    })
                    // ================ TriggerRegisterEmail Lambda ================
                    const response = fetch('https://27npsn2kfe.execute-api.ap-southeast-1.amazonaws.com/beta', {
                        method: "POST",
                        body: bodyJSON,
                        headers: {
                            "Content-type": "application/json"
                        }
                    })
                    .then((response) => response.json()) 
                    .then(data => {
                        console.log(data);
                        this.emailTriggerSuccessCode = data.statusCode;
                    })
                    .catch(error => {
                        console.log(error);
                    })
        
                    console.log(this.emailTriggerSuccessCode);
                    //router push
                    this.$router.push('/cartCheckout')
                    localStorage.setItem("email", this.userEmail)
                }
            } catch(err) {
                console.log(err)
                alert("Email is already registered!")
            }
        },
        async login() {
            console.log("login")

            let res = await this.logIn({'email': this.userEmail, 'password': this.userPassword});
            console.log(res)

            try {
                if (res.code == 200) {
                    //router push
                    this.$router.push('/cartCheckout')
    
                    localStorage.setItem("email", res.email)
                } else {
                    console.log(res.message)
                }
            } catch(err) {
                console.log(err)
                alert("Incorrect email or password, please try again!")
            }

        }
    }
}
</script>
