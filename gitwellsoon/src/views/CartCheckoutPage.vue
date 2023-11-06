<template>
    <div class="container-fluid mt-5 mb-5">

        <!-- ****** Checkout Area Start ****** -->
        <div class="checkout_area section_padding_100">
            <div class="container">
                <div class="row">

                    <div class="col-12 col-md-6">
                        <div class="checkout_details_area mt-50 clearfix">

                            <div class="cart-page-heading">
                                <h5>Billing Address</h5>
                            </div>

                            <form action="#" method="post">
                                <div class="row">
                                    <div class="col-12 mb-3">
                                        <label for="first_name">Name<span>*</span></label>
                                        <input type="text" class="form-control" id="first_name" value="" required>
                                    </div>
                                    <div class="col-12 mb-3">
                                        <label for="company">Company Name</label>
                                        <input type="text" class="form-control" id="company" value="">
                                    </div>
                                    <div class="col-12 mb-3">
                                        <label for="country">Country <span>*</span></label>
                                        <select class="custom-select d-block w-100" id="country">
                                        <option value="usa">Singapore</option>
                                        <option value="uk">Hong Kong</option>
                                    </select>
                                    </div>
                                    <div class="col-12 mb-3">
                                        <label for="street_address">Address <span>*</span></label>
                                        <input type="text" class="form-control mb-3" id="street_address" value="">
                                        <input type="text" class="form-control" id="street_address2" value="">
                                    </div>
                                    <div class="col-12 mb-3">
                                        <label for="postcode">Postcode <span>*</span></label>
                                        <input type="text" class="form-control" id="postcode" value="">
                                    </div>
                                    <div class="col-12 mb-3">
                                        <label for="city">Town/City <span>*</span></label>
                                        <input type="text" class="form-control" id="city" value="">
                                    </div>
                                    <div class="col-12 mb-3">
                                        <label for="state">Province <span>*</span></label>
                                        <input type="text" class="form-control" id="state" value="">
                                    </div>
                                    <div class="col-12 mb-3">
                                        <label for="phone_number">Phone No <span>*</span></label>
                                        <input type="number" class="form-control" id="phone_number" min="0" value="">
                                    </div>
                                    <div class="col-12 mb-4">
                                        <label for="email_address">Email Address <span>*</span></label>
                                        <input type="email" class="form-control" id="email_address" value="">
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>

                    <div class="col-12 col-md-6 col-lg-5 ml-lg-auto">
                        <div class="order-details-confirmation">

                            <div class="cart-page-heading">
                                <h5>Your Order</h5>
                                <p>The Details</p>
                            </div>

                            <ul class="order-details-form mb-4">
                                <li class="bg-info px-3"><span><strong>Product</strong></span> <span><strong>Total</strong></span></li>
                                <li v-for="oneItem in cart_item" class="px-3">
                                    <span>{{oneItem.productName}}</span> <span>${{oneItem.total_item_price}}</span>
                                </li>
                                <li class="bg-info px-3"><span>Subtotal</span> <span>${{total_price}}</span></li>
                                <li class="bg-info px-3"><span>Shipping</span> <span>${{shippingMethod}}</span></li>
                                <li class="bg-info px-3"><span>Total</span> <span>${{final_price}}</span></li>
                            </ul>


                            <div id="accordion" role="tablist" class="mb-4">
                                <div class="card">
                                    <div class="card-header" role="tab" id="headingTwo">
                                        <h6 class="mb-0">
                                            <input type="radio" id="cd" name="payment" value="cd">
                                            <label for="cd" class="ms-3">Cash on Delivery</label><br>
                                        </h6>
                                    </div>
                                </div>
                                <div class="card">
                                    <div class="card-header" role="tab" id="headingThree">
                                        <h6 class="mb-0">
                                            <input type="radio" id="cc" name="payment" value="cc">
                                            <label for="cc" class="ms-3">Credit Card</label><br>
                                        </h6>
                                    </div>
                                </div>
                               
                            </div>

                            <!-- <router-link to="/paymentSuccess"> -->
                                <!-- <a href="./paymentsuccess.html" class="btn karl-checkout-btn" style="background-color:#0CC0DF">Place Order</a> -->
                                <a class="btn karl-checkout-btn" @click="callTriggerPayment()" style="background-color:#0CC0DF">Place Order</a>
                            <!-- </router-link> -->
                        </div>
                    </div>

                </div>
            </div>
        <!-- ****** Checkout Area End ****** -->
        </div>

    </div>
</template>
<script>
import axios from "axios";

export default {
    name: "CartPage",
    components: {
    },
    data(){
        return {
            cart_item: [],
            total_price: 0,
            shippingMethod: 0,
            final_price: 0
        }
    },
    async mounted() {
       this.cart_item = JSON.parse(localStorage.getItem("cartItem"));

        this.total_price = JSON.parse(localStorage.getItem("subtotal"));
        this.shippingMethod = JSON.parse(localStorage.getItem("shipping"));
        this.final_price = JSON.parse(localStorage.getItem("finaltotal"));
    },
    computed: {
    },
    methods: {
        sendPage(pid) {
            localStorage.setItem("selectedItem", pid);
        },
        tabulateFinalPrice() {
            this.final_price = this.total_price + this.shippingMethod;
        },
        callTriggerPayment() {
            // TriggerPayment
            axios.get("https://uxgheebrgoi7mbz26szg7c6ffe0zpzyg.lambda-url.ap-southeast-1.on.aws/")
            .then(response =>{
                console.log(response)
            })
            .catch(error => alert(error))
            // const response = fetch('https://uxgheebrgoi7mbz26szg7c6ffe0zpzyg.lambda-url.ap-southeast-1.on.aws/')
            // .then((response) => response.json()) 
            // .then(data => {
            //     console.log(data);
            //     return data.statusCode;
            // })
            // .catch(error => {
            //     console.log(error);
            // })
        },
        // TriggerPayment
        // https://uxgheebrgoi7mbz26szg7c6ffe0zpzyg.lambda-url.ap-southeast-1.on.aws/

        // TriggerRegisterEmail
        // https://t5koenoe6ciiufp4cimt34cng40imejk.lambda-url.ap-southeast-1.on.aws/ 

        // TriggerSendEmail
        // https://h54bsx4ar5iywpwfe5endxgj4m0bgubt.lambda-url.ap-southeast-1.on.aws/
    },
}
</script>

<style>

/* -----------------------
:: 19.0 Checkout Area CSS
----------------------- */

.checkout_details_area form label {
    font-size: 12px;
    text-transform: uppercase;
}

.checkout_details_area form label span {
    color: #ff084e;
}

.checkout_details_area form .form-control,
.checkout_details_area form .custom-select {
    height: 52px;
    border: none;
    background-color: #CFD6E1;
    border-radius: 0;
}

.order-details-confirmation {
    width: 100%;
    border: 2px solid #ebebeb;
    padding: 40px;
}

.order-details-confirmation .order-details-form li {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    margin-bottom: 20px;
    font-size: 12px;
    text-transform: uppercase;
    padding: 30px 0;
    border-bottom: 2px solid #ebebeb;
}

.order-details-confirmation .card-header h6 a {
    display: block;
    font-size: 12px;
    text-transform: uppercase;
}

.order-details-confirmation .card-header h6 a i {
    color: #9f9f9f;
}

.order-details-confirmation .card {
    border: none;
}

.order-details-confirmation .card-header {
    background-color: transparent;
    border-bottom: none;
}

.order-details-confirmation .card-body p {
    font-size: 12px;
    line-height: 2;
    color: #9f9f9f;
}

/*....*/
.createaccount{
    width: 100%; 
    text-align: center; 
    border-bottom: 1px solid #000; 
    line-height: 0.1em;
    margin: 10px 0 20px; 
}

.createaccount span{
    background:#fff; 
    padding:0 10px; 
}

.karl-checkout-btn {
    width: 100%;
    height: 60px;
    background-color: #0cc0df;
    border-radius: 0;
    color: #fff;
    text-transform: uppercase;
    font-weight: 700;
    line-height: 60px;
    padding: 0;
}


.karl-checkout-btn:hover,
.karl-checkout-btn:focus {
    background-color: #3a3a3a;
    color: #fff;
    font-weight: 700;
}
</style>