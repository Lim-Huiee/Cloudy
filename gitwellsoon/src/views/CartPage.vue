<template>
    <div class="container-fluid">

        <!-- ****** Cart Area Start ****** -->
        <div id="main-container">
            <div class="cart_area clearfix mt-5 mb-5">
                <div class="container">
                    <div class="row">
                        <div class="col-12">
                            <div class="cart-table clearfix">
                                <table class="table table-responsive">
                                    <thead>
                                        <tr>
                                            <th>Product</th>
                                            <th>Price</th>
                                            <th>Quantity</th>
                                            <th>Total</th>
                                            <th></th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="oneItem in cart_item">
                                            <td class="cart_product_img d-flex align-items-center">
                                                <a href="#"><img :src="oneItem.image" alt="Product" style="width:100%;"></a>
                                                <h6>{{oneItem.productName}}</h6>
                                            </td>
                                            <td class="price"><span>{{oneItem.price}}</span></td>
                                            <td class="qty">
                                                <div class="quantity">
                                                    <span class="qty-text" id="qty" name="quantity" :value="oneItem.qty" style="font-size:large;">{{oneItem.qty}}</span>
                                                </div>
                                            </td>
                                            <td class="total_price"><span>${{oneItem.total_item_price}}</span></td>
                                            <td><i style="font-size:20px; color:red;cursor:pointer;" class="fa" @click="removeItem(oneItem)">&#xf00d;</i></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
        
                        </div>
                    </div>
        
                    <div class="row">
                        <div class="col-12 col-md-6 col-lg-4">
                            <div class="coupon-code-area mt-70">
                                <div class="cart-page-heading">
                                    <h5>Coupon code</h5>
                                    <p>Enter your Coupon code</p>
                                </div>
                                <form action="#">
                                    <input type="search" name="search" placeholder="#569ab15">
                                    <button type="submit">Apply</button>
                                </form>
                            </div>
                        </div>
                        <div class="col-12 col-md-6 col-lg-4">
                            <div class="shipping-method-area mt-70">
                                <div class="cart-page-heading">
                                    <h5>Shipping method</h5>
                                    <p>Select the one you want</p>
                                </div>
                                

                                <div class="custom-control custom-radio mb-30" @change="tabulateFinalPrice">
                                    <input type="radio" id="customRadio2" name="customRadio" class="custom-control-input" :value="1.99" v-model="shippingMethod">
                                    <label class="custom-control-label d-flex align-items-center justify-content-between" for="customRadio2"><span>Standard delivery</span><span>$1.99</span></label>

                                    <input type="radio" id="customRadio3" name="customRadio" class="custom-control-input" :value="0" v-model="shippingMethod">
                                    <label class="custom-control-label d-flex align-items-center justify-content-between" for="customRadio3"><span>Personal Pickup</span><span>Free</span></label>
                                </div>

                            </div>
                        </div>
                        <div class="col-12 col-lg-4">
                            <div class="cart-total-area mt-70">
                                <div class="cart-page-heading">
                                    <h5>Cart total</h5>
                                    <p>Final info</p>
                                </div>
        
                                <ul class="cart-total-chart">
                                    <li><span>Subtotal</span> <span>${{total_price}}</span></li>
                                    <li><span>Shipping</span> <span>${{shippingMethod}}</span></li>
                                    <li><span><strong>Total</strong></span> <span><strong>${{final_price}}</strong></span></li>
                                </ul>
                                <router-link to="/UserLogin">
                                    <a class="btn karl-checkout-btn" @click="sendPage()">Proceed to checkout</a>
                                </router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- ****** Cart Area End ****** -->

    </div>
</template>

<script>
export default {
    name: "CartPage",
    components: {
    },
    data(){
        return {
            cart_item: [],
            total_price: 0,
            shippingMethod: 0,
            final_price: 0,
        }
    },
    async mounted() {
        this.cart_item = JSON.parse(localStorage.getItem("cartItem"));
        console.log(this.cart_item);

        for (let i = 0; i < this.cart_item.length; i++) {
            this.total_price += this.cart_item[i]["total_item_price"]
        }

        this.final_price = this.total_price;
    },
    computed: {
        getQty() {
            if (JSON.parse(localStorage.getItem("cartQty"))) {
                this.cart_qty = JSON.parse(localStorage.getItem("cartQty"));
            }
            return this.cart_qty;
        }
    },
    methods: {
        sendPage() {
            localStorage.setItem("subtotal", this.total_price);
            localStorage.setItem("shipping", this.shippingMethod);
            localStorage.setItem("finaltotal", this.final_price);
        },
        tabulateFinalPrice() {
            this.final_price = this.total_price + this.shippingMethod;
        },
        removeItem(item) {
            console.log(this.cart_item);
            console.log(item);
            var item_index = this.cart_item.findIndex(cartItem => cartItem === item);
            this.cart_item.splice(item_index, 1);
            console.log(this.cart_item);

            localStorage.setItem('cartItem', JSON.stringify(this.cart_item));
            this.cart_item = JSON.parse(localStorage.getItem("cartItem"));

            
            var existing_qty = JSON.parse(localStorage.getItem("cartQty"));
            var new_qty = existing_qty - item.qty;
            localStorage.setItem('cartQty', new_qty);

            location.reload();
        }
    },
}
</script>

<style scoped>
/* -------------------
:: 18.0 Cart Page CSS
------------------- */

.cart-table .table {
    position: relative;
    z-index: 9;
}

.cart_area table thead {
    background-color: #CFD6E1;
    border: none;
}

.cart_area table tbody tr td {
    width: 10% !important;
}

.cart_area table tbody tr td:first-child {
    width: 70% !important;
}

.cart_product_img > a {
    width: 120px;
    margin-right: 20px;
}

.cart-table .table td,
.cart-table .table th {
    padding: 12px;
    padding: 12px;
    padding: 0.75rem;
    text-align: left;
    vertical-align: middle;
    border: none;
    font-size: 13px;
}

.cart-table .cart_product_img h6 {
    font-size: 14px;
    margin: 0;
    font-weight: 400;
}

.cart-table .qty-minus,
.cart-table .qty-plus {
    background-color: #f6f6f6;
    cursor: pointer;
    display: inline-block;
    height: 30px;
    width: 30px;
}

.cart-table .qty-minus i,
.cart-table .qty-plus i {
    line-height: 30px;
    font-size: 10px;
}

.cart-table .qty-text {
    background-color: #f6f6f6;
    border: medium none;
    display: inline-block;
    height: 30px;
    -moz-appearance: textfield;
    -webkit-appearance: textfield;
    appearance: textfield;
    text-align: center;
    font-size: 12px;
    width: 50px;
}

.cart-table .quantity {
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    display: -webkit-inline-box;
    display: -ms-inline-flexbox;
    display: inline-flex;
    text-align: center;
}

.cart-table .price span,
.cart-table .total_price > span,
.cart-table .action > a {
    font-size: 14px;
}

.cart_area .update-checkout a,
.cart_area .back-to-shop a {
    background-color: transparent;
    border-radius: 0;
    display: inline-block;
    height: 55px;
    line-height: 51px;
    min-width: 120px;
    padding: 0 30px;
    text-align: center;
    font-size: 14px;
    font-weight: 700;
    border: 2px solid #3a3a3a;
    text-transform: uppercase;
}

.cart_area .update-checkout a:first-child {
    color: #7a7a7a;
    border-color: #CFD6E1;
}

.cart_area .update-checkout a:last-child {
    background-color: #CFD6E1;
    color: #7a7a7a;
    border-color: #CFD6E1;
}

.cart-page-heading {
    margin-bottom: 50px;
}

.cart-page-heading h5 {
    text-transform: uppercase;
    font-size: 18px;
}

.cart-page-heading p {
    color: #7a7a7a;
    font-size: 14px;
    margin-bottom: 0;
}

.coupon-code-area form {
    position: relative;
    z-index: 1;
}

.coupon-code-area form > input {
    width: 100%;
    height: 52px;
    border: none;
    background-color: #f2f7f8;
    padding: 0 30px;
    font-size: 12px;
}

.coupon-code-area form > button {
    width: 120px;
    height: 52px;
    border: none;
    text-transform: uppercase;
    background-color: #0cc0df;
    padding: 0 30px;
    font-size: 14px;
    position: absolute;
    top: 0;
    color: #fff;
    font-weight: 700;
    right: 0;
}

.shipping-method-area .custom-control-label span {
    font-size: 14px;
}

.cart-total-chart {
    background-color: #CFD6E1;
    padding: 30px;
}

.cart-total-chart li {
    display: -moz-flex;
    display: -ms-flex;
    display: -o-flex;
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