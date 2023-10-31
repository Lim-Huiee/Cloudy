<template>
    <div class="container-fluid">

        <div class="container" id="main-container">
                
            <div class="row justify-content-center mt-5 mb-5">
                <div class="col-4 col-md-4 col-lg-4 ml-lg-auto">
                    <div class="order-details-confirmation">

                        <div class="cart-page-heading">
                            <h5>Manage profile</h5>
                            <p>The Details</p>
                        </div>

                        <ul class="order-details-form mb-4" style="padding-left:0px">
                            <li class="bg-info px-3" @click="changeView('trackOrder')" style="cursor:pointer;"><span>Track Order</span></li>
                            <li class="bg-info px-3" @click="changeView('transHist')" style="cursor:pointer;"><span>Transaction History</span> </li>
                            <li class="bg-info px-3" @click="changeView('profile')" style="cursor:pointer;"><span>Manage Profile</span></li>
                        </ul>
                    </div>
                </div>
                <div class="col-8" v-if="view==='profile'">
                    <div class="checkout_details_area mt-50 clearfix">
            
                        <div class="cart-page-heading text-center">
                            <h5>Profile</h5>
                        </div>
            
                        <form action="#" method="post">
                            <div class="row">
                                <div class="col-md-12 mb-3">
                                    <label for="first_name">Name <span>*</span></label>
                                    <input type="text" class="form-control" id="first_name" value="" :disabled="!edit">
                                </div>
                                <div class="col-12 mb-3">
                                    <label for="company">Company Name</label>
                                    <input type="text" class="form-control" id="company" value="" :disabled="!edit">
                                </div>
                                <div class="col-12 mb-3">
                                    <label for="country">Country <span>*</span></label>
                                    <select class="custom-select d-block w-100" id="country" :disabled="!edit">
                                        <option value="usa">Singapore</option>
                                        <option value="uk">Hong Kong</option>
                                    </select>
                                </div>
                                <div class="col-12 mb-3">
                                    <label for="street_address">Address <span>*</span></label>
                                    <input type="text" class="form-control mb-3" id="street_address" value=""  :disabled="!edit">
                                    <input type="text" class="form-control" id="street_address2" value=""  :disabled="!edit">
                                </div>
                                <div class="col-12 mb-3">
                                    <label for="postcode">Postcode <span>*</span></label>
                                    <input type="text" class="form-control" id="postcode" value=""  :disabled="!edit">
                                </div>
                                <div class="col-12 mb-3">
                                    <label for="city">Town/City <span>*</span></label>
                                    <input type="text" class="form-control" id="city" value="" :disabled="!edit">
                                </div>
                                <div class="col-12 mb-3">
                                    <label for="state">Province <span>*</span></label>
                                    <input type="text" class="form-control" id="state" value="" :disabled="!edit">
                                </div>
                                <div class="col-12 mb-3">
                                    <label for="phone_number">Phone No <span>*</span></label>
                                    <input type="number" class="form-control" id="phone_number" min="0" value="" :disabled="!edit">
                                </div>
                                <div class="col-12 mb-4">
                                    <label for="email_address">Email Address <span>*</span></label>
                                    <input type="email" class="form-control" id="email_address" value="" :disabled="!edit">
                                </div>

                                <div class="col-12">
                                    <div class="btn karl-checkout-btn mt-2" style="background-color:#0CC0DF" v-if="edit" @click="editField()">Confirm update</div>
                                    <div class="btn karl-checkout-btn mt-2 mb-4" style="background-color:#0CC0DF" v-else @click="editField()">Edit</div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            
                <div class="col-8" v-if="view === 'transHist'">
                    <div class="checkout_details_area mt-50 clearfix">
            
                        <div class="cart-page-heading text-center">
                            <h5>Transaction history</h5>
                        </div>
                    </div>

                </div>

                <div class="col-8" v-if="view === 'trackOrder'">
                    <div class="checkout_details_area mt-50 clearfix">
            
                        <div class="cart-page-heading text-center">
                            <h5>Track order</h5>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "CartPage",
    components: {
    },
    data(){
        return {
            view: 'profile',
            edit: false
        }
    },
    async mounted() {
    },
    computed: {
    },
    methods: {
        editField() {
            this.edit = !this.edit; 
        },
        changeView(selectedView) {
            this.view = selectedView;
        }
    },
}
</script>
