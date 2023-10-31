<template>
    <div class="container-fluid">
        <div class="row">
            <nav class="navbar navbar-expand-lg bg-dark navbar-light d-none d-lg-block" id="templatemo_nav_top">
                <div class="container text-light">
                    <div class="w-100 d-flex justify-content-between">
                        <div>
                            <i class="fa fa-envelope mx-2"></i>
                            <a class="navbar-sm-brand text-light text-decoration-none" href="mailto:info@company.com">info@gitwellsoon.com</a>
                            <i class="fa fa-phone mx-2"></i>
                            <a class="navbar-sm-brand text-light text-decoration-none" href="tel:010-020-0340">000-000-000</a>
                        </div>
                    </div>
                </div>
            </nav>

            <nav class="navbar navbar-expand-lg navbar-light shadow">
                <div class="container d-flex justify-content-between align-items-center">

                    <a class="navbar-brand text-info logo h1 align-self-center">
                        <router-link to="/">
                            <img src="../assets/logo/Git Well Soon (Transparent).png" style="width:25%;">
                        </router-link>
                    </a>


                    <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#templatemo_main_nav" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>

                    <div class="align-self-center collapse navbar-collapse flex-fill  d-lg-flex justify-content-lg-between" id="templatemo_main_nav">
                        <div class="flex-fill">
                            <ul class="nav navbar-nav d-flex justify-content-between mx-lg-auto">
                                <li class="nav-item">
                                    <router-link to="/" class="nav-link text-decoration-none">Home</router-link>
                                </li>
                                <li class="nav-item">
                                    <router-link to="/shop" class="nav-link text-decoration-none">Shop</router-link>
                                </li>
                                <li class="nav-item">
                                    <router-link to="/about" class="nav-link text-decoration-none">About Us</router-link>
                                </li>
                                <li class="nav-item">
                                    <router-link to="/contact" class="nav-link text-decoration-none">Contact</router-link>
                                </li>
                            </ul>
                            
                        </div>
                        <div class="navbar align-self-center d-flex" id="cart-nav">
                            <div class="d-lg-none flex-sm-fill mt-3 mb-4 col-7 col-sm-auto pr-3">
                                <div class="input-group">
                                    <input type="text" class="form-control" id="inputMobileSearch" placeholder="Search ...">
                                    <div class="input-group-text">
                                        <i class="fa fa-fw fa-search"></i>
                                    </div>
                                </div>
                            </div>
                            <a class="nav-icon d-none d-lg-inline" href="#" data-bs-toggle="modal" data-bs-target="#templatemo_search">
                                <i class="fa fa-fw fa-search text-dark mr-2"></i>
                            </a>
                            <a class="nav-icon position-relative text-decoration-none">
                                <router-link to="/cart" class="nav-link text-decoration-none">
                                    Cart
                                    <span class="position-absolute top-0 left-100 translate-middle badge rounded-pill bg-light text-dark">{{cart_qty}}</span>
                                </router-link>
                                <!-- <i class="fa fa-fw fa-cart-arrow-down text-dark mr-1">Cart</i> -->
                            </a>
                            <a class="nav-icon position-relative text-decoration-none" href="./profile.html">

                                <router-link to="/profile" class="nav-link text-decoration-none">
                                    Profile
                                </router-link>
                                <!-- <i class="fa fa-fw fa-user text-dark mr-3">Profile</i> -->
                                <span class="position-absolute top-0 left-100 translate-middle badge rounded-pill bg-light text-dark"></span>
                            </a>
                        </div>
                    </div>
                </div>
            </nav>
        </div>

        <div class="row">
            <div class="content-body">
                <router-view/>
            </div>
            <pageFooter></pageFooter>
        </div>
    </div>

</template>

<script>
import pageFooter from "./pageFooter.vue";

export default {
    name: "navBar",
    components: {
        pageFooter
    }
}

</script>

<style scoped>

.content-body{
    min-height: 100vh;
}

/* Nav */
#templatemo_nav_top { min-height: 40px;}
#templatemo_nav_top * { font-size: .9em !important;}
#templatemo_main_nav a { color: #212934;}
#templatemo_main_nav a:hover { color: #0cc0df;}
#templatemo_main_nav .navbar .nav-icon { margin-right: 20px;}
</style>