<template>
    <div class="container-fluid">

    <!-- Start Content -->
    <div class="container py-5">
        <div class="row">
            <div class="col-lg-3">
                <h1 class="h2 pb-4">Categories</h1>

                <ul class="list-unstyled templatemo-accordion">
                    <li class="pb-3">
                        <a class="d-flex justify-content-between h3 text-decoration-none" href="#">
                            <h3>Monitoring</h3>
                        </a>
                        <ul class="show list-unstyled pl-3">
                            <li><a class="text-decoration-none" href="#" @click="changeView('bpm')">Blood Pressure Monitor</a></li>
                            <li><a class="text-decoration-none" href="#" @click="changeView('ventilator')">Ventilators</a></li>
                        </ul>
                    </li>
                    <li class="pb-3">
                        <a class="d-flex justify-content-between h3 text-decoration-none" href="#">
                            <h3>Medical Equipments</h3>
                        </a>
                        <ul class="list-unstyled pl-3">
                            <li><a class="text-decoration-none" href="#" @click="changeView('wc')">Wheelchairs</a></li>
                            <li><a class="text-decoration-none" href="#" @click="changeView('ivdrip')">IV Drips</a></li>
                        </ul>
                    </li>

                    <li class="pb-3">
                        <a class="d-flex justify-content-between h3 text-decoration-none" href="#">
                            <h3>Accessories</h3>
                        </a>
                        <ul class="list-unstyled pl-3" >
                            <li><a class="text-decoration-none" href="#" @click="changeView('bandage')">Bandage</a></li>
                            <li><a class="text-decoration-none" href="#" @click="changeView('fm')">Face Mask</a></li>
                            <li><a class="text-decoration-none" href="#" @click="changeView('fak')">First Aid Kit</a></li>
                            <li><a class="text-decoration-none" href="#" @click="changeView('glove')">Gloves</a></li>
                            <li><a class="text-decoration-none" href="#" @click="changeView('hs')">Hand Sanitizer</a></li>
                            <li><a class="text-decoration-none" href="#" @click="changeView('support')">Supporting guards</a></li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class="col-lg-9">
                <div class="row">
                    <div class="col-md-4" v-for="OneListing in selected_list">
                        <div class="card mb-4 product-wap rounded-0">
                            <div class="card rounded-0">
                                <img class="card-img rounded-0 img-fluid" :src="OneListing.image">
                                <div class="card-img-overlay rounded-0 product-overlay d-flex align-items-center justify-content-center">
                                    <ul class="list-unstyled">
                                        <li><router-link to="/shopProduct" class="btn btn-success text-white mt-2" @click="sendPage(OneListing)"><i class="bi bi-eye"></i></router-link></li>
                                    </ul>
                                </div>
                            </div>
                            <div class="card-body">
                                <a href="shop-single.html" class="h3 text-decoration-none">{{OneListing.productName}}</a>
                                <ul class="w-100 list-unstyled d-flex justify-content-between mb-0">
                                    <li class="pt-2">
                                        <span class="product-color-dot color-dot-red float-left rounded-circle ml-1"></span>
                                        <span class="product-color-dot color-dot-blue float-left rounded-circle ml-1"></span>
                                        <span class="product-color-dot color-dot-black float-left rounded-circle ml-1"></span>
                                        <span class="product-color-dot color-dot-light float-left rounded-circle ml-1"></span>
                                        <span class="product-color-dot color-dot-green float-left rounded-circle ml-1"></span>
                                    </li>
                                </ul>
                                <ul class="list-unstyled d-flex justify-content-center mb-1">
                                    <li>
                                        <i class="text-warning fa fa-star"></i>
                                        <i class="text-warning fa fa-star"></i>
                                        <i class="text-warning fa fa-star"></i>
                                        <i class="text-muted fa fa-star"></i>
                                        <i class="text-muted fa fa-star"></i>
                                    </li>
                                </ul>
                                <p class="text-center mb-0">${{OneListing.price}}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
    <!-- End Content -->

    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default {
    name: "ShopPage",
    components: {
    },
    data(){
        return {
            view: 'bpm',
            product_list: {
                bandage_list: [{
                        pid: '1',
                        productName: 'Johnson&Johnson Band-Aid skin-flex',
                        image: '../assets/Product Data/bandage1.jpeg',
                        desc: 'desc1',
                        price: '10.00'
                    }, {
                        pid: '2',
                        productName: 'Johnson&Johnson Band-Aid flexible fabric',
                        image: '../assets/Product Data/bandage2.jpeg',
                        desc: 'desc2',
                        price: '6.00'
                    }],
                ventilator_list: [{
                        pid: '3',
                        productName: 'ventilator 1',
                        image: '../assets/Product Data/ventilator1.jpeg',
                        desc: 'desc3',
                        price: '120.00'
                    }],
                wc_list: [{ 
                        pid: '4',
                        productName: 'Karma foldable wheelchair',
                        image: '../assets/Product Data/wc1.jpeg',
                        desc: 'desc4',
                        price: '480.00'
                    }, {
                        pid: '5',
                        productName: 'Karma wheelchair',
                        image: '../assets/Product Data/wc2.jpeg',
                        desc: 'desc5',
                        price: '200.00'
                    }],
                ivdrip_list: [{
                        pid: '6',
                        productName: 'IV treatment',
                        image: '../assets/Product Data/ivdrip1.jpeg',
                        desc: 'desc6',
                        price: '60.00'
                    }],
                bpm_list: [{
                        pid: '7',
                        productName: 'Omron blood pressure monitor',
                        image: '../assets/Product Data/bpm1.jpeg',
                        desc: 'desc7',
                        price: '100.00'
                    }],
                fm_list:[{
                        pid: '8',
                        productName: 'Alertcare 3-ply Face Mask',
                        image: '../assets/Product Data/facemask2.jpeg',
                        desc: 'desc8',
                        price: '12.00'     
                    }],
                fak_list: [{
                        pid: '9',
                        productName: 'Hypa First Aid Kit',
                        image: '../assets/Product Data/fak2.jpeg',
                        desc: 'desc9',
                        price: '24.00'
                    }],
                glove_list:[{
                        pid: '10',
                        productName: 'Nitrile Gloves',
                        image: '../assets/Product Data/glove5.jpeg',
                        desc: 'desc10',
                        price: '6.00'
                    }],
                support_list:[{
                        pid: '11',
                        productName: 'Futuro Wrist Support',
                        image: '../assets/Product Data/support2.jpeg',
                        desc: 'desc11',
                        price: '12.00'
                    }, {
                        pid: '12',
                        productName: 'Ugoku Knee Support',
                        image: '../assets/Product Data/support5.jpeg',
                        desc: 'desc12',
                        price: '15.00'  
                    }],
                hs_list: [{
                        pid: '13',
                        productName: 'Lifebuoy Hand Sanitizer',
                        image: '../assets/Product Data/hs3.jpeg',
                        desc: 'desc13',
                        price: '3.00'
                    }]
            },
            selected_list:[{
                        pid: '7',
                        productName: 'Omron blood pressure monitor',
                        image: '../assets/Product Data/bpm1.jpeg',
                        desc: 'desc14',
                        price: '100.00'
                    }]
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
        changeView(selectedView) {
            this.selected_list = this.product_list[selectedView + '_list'];
            console.log(this.selected_list);
        },
        sendPage(oneList) {
            localStorage.setItem("selectedItem", JSON.stringify(oneList));
        }
    },
}
</script>
