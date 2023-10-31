<template>
    <div class="container-fluid">
        <section class="bg-success py-5">
            <div class="container">
                <div class="row align-items-center py-5">
                    <div class="col-md-8 text-white">
                        <h1>About Us</h1>
                        <p>
                            At Git Well Soon, we are dedicated to making healthcare accessible and convenient for everyone. 
                            As a leading online shopping platform for medical supplies, our mission is to provide, individuals, healthcare professionals, and organisations with a one-stop solution for their medical needs.
                        </p>
                    </div>
                    <div class="col-md-4">
                        <img src="../assets/about-hero.svg" alt="About Hero">
                    </div>
                </div>
            </div>
        </section>
        <!-- Close Banner -->

        <!-- Start Section -->
        <section class="container py-5">
            <div class="row text-center pt-5 pb-3">
                <div class="col-lg-6 m-auto">
                    <h1 class="h1">Our Services</h1>
                </div>
            </div>
            <div class="row">

                <div class="col-md-6 col-lg-3 pb-5">
                    <div class="h-100 py-5 services-icon-wap shadow">
                        <div class="h1 text-success text-center"><i class="fa fa-truck fa-lg"></i></div>
                        <h2 class="h5 mt-4 text-center">Delivery Services</h2>
                    </div>
                </div>

                <div class="col-md-6 col-lg-3 pb-5">
                    <div class="h-100 py-5 services-icon-wap shadow">
                        <div class="h1 text-success text-center"><i class="fas fa-exchange-alt"></i></div>
                        <h2 class="h5 mt-4 text-center">Shipping & Return</h2>
                    </div>
                </div>

                <div class="col-md-6 col-lg-3 pb-5">
                    <div class="h-100 py-5 services-icon-wap shadow">
                        <div class="h1 text-success text-center"><i class="fa fa-percent"></i></div>
                        <h2 class="h5 mt-4 text-center">Promotion</h2>
                    </div>
                </div>

                <div class="col-md-6 col-lg-3 pb-5">
                    <div class="h-100 py-5 services-icon-wap shadow">
                        <div class="h1 text-success text-center"><i class="fa fa-user"></i></div>
                        <h2 class="h5 mt-4 text-center">24 Hours Service</h2>
                    </div>
                </div>
            </div>
        </section>
        <!-- End Section -->
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default {
    name: "AboutPage",
    components: {
    },
    data(){
        return {
            cart_qty: 0
        }
    },
    async mounted() {
        if (JSON.parse(localStorage.getItem("cartQty"))) {
            this.cart_qty = JSON.parse(localStorage.getItem("cartQty"));
        }
    },
    computed: {
    },
    methods: {
    },
}


//  const topbar = Vue.createApp({
//             data() {
//                 return {
//                     cart_qty: 0
//                 }
//             },
//             mounted: function(){
//                 if (JSON.parse(localStorage.getItem("cartQty"))) {
//                     this.cart_qty = JSON.parse(localStorage.getItem("cartQty"));
//                 }
//             },
//             computed: {
//             },
//             methods: {
//             }
//         }).mount("#cart-nav");
</script>