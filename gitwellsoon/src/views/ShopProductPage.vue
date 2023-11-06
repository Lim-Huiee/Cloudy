<template>
    <div class="container-fluid">

        <!-- Open Content -->
        <section class="bg-light" id="main-container">
            <div class="container pb-5">
                <div class="row">
                    <div class="col-lg-5 mt-5">
                        <div class="card mb-3">
                            <img class="card-img img-fluid" :src="selected_item_image" alt="Error loading Image" id="product-detail">
                        </div>
                    </div>
                    <!-- col end -->
                    <div class="col-lg-7 mt-5">
                        <div class="card">
                            <div class="card-body">
                                <h1 class="h2">{{selected_item.pname}}</h1>
                                <p class="h3 py-2">${{selected_item.pprice}}</p>
                                <!-- <p class="py-2">
                                    <i class="fa fa-star text-warning"></i>
                                    <i class="fa fa-star text-warning"></i>
                                    <i class="fa fa-star text-warning"></i>
                                    <i class="fa fa-star text-warning"></i>
                                    <i class="fa fa-star text-secondary"></i>
                                    <span class="list-inline-item text-dark">Rating 4.8 | 36 Comments</span>
                                </p> -->

                                <h6>Description:</h6>
                                <p>{{selected_item.pdesc}}</p>

                                <h6>Stock: <span>{{selected_item.stock}}</span></h6>
                                <br>
                                <h6>Production date:</h6>
                                <p>{{selected_item.prod_date}}</p>

                                <h6>Expiry date:</h6>
                                <p>{{selected_item.expiry_date}}</p>

                                    <input type="hidden" name="product-title" value="Activewear">
                                    <div class="row">
                                        <div class="col-auto">
                                            <ul class="list-inline pb-3">
                                                <li class="list-inline-item text-right">
                                                    Quantity
                                                    <input type="hidden" name="product-quanity" id="product-quanity" :value="qty">
                                                </li>
                                                <li class="list-inline-item"><span class="btn btn-success" @click="qty--">-</span></li>
                                                <li class="list-inline-item"><span class="badge bg-secondary" id="var-value">{{qty}}</span></li>
                                                <li class="list-inline-item"><span class="btn btn-success" @click="qty++">+</span></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="row pb-3">
                                        <div class="col d-grid">
                                            <button type="submit" class="btn btn-success btn-lg" name="submit" value="addtocard" @click="addToCart()">Add To Cart</button>
                                        </div>
                                    </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Close Content -->

    </div>
</template>

<script>
export default {
    name: "ShopProductPage",
    components: {
    },
    data(){
        return {
            selected_item: [],
            qty: 1,
            selected_item_image: ""
        }
    },
    async mounted() {
        this.selected_item = JSON.parse(localStorage.getItem("selectedItem"));
        this.selected_item_image = JSON.parse(localStorage.getItem("selectedItemImg"))
    },
    computed: {
    },
    methods: {
        addToCart() {
            this.selected_item['qty'] = this.qty;
            this.selected_item['total_item_price'] = this.qty * this.selected_item.pprice;

            if (JSON.parse(localStorage.getItem("cartItem"))) {
                var cart_items = JSON.parse(localStorage.getItem("cartItem"));
                var filtered_cart = cart_items.filter( item => item.pid === this.selected_item.pid );
                if (filtered_cart.length > 0) {
                    var item_index = cart_items.findIndex(item => item.pid === this.selected_item.pid);
                    cart_items[item_index]['qty'] += this.selected_item['qty']; 
                    cart_items[item_index]['total_item_price'] = cart_items[item_index]['qty'] * cart_items[item_index].pprice;
                }  else {
                    cart_items.push(this.selected_item);
                }
            } else {
                var cart_items = [];
                cart_items.push(this.selected_item);
            }
            localStorage.setItem('cartItem', JSON.stringify(cart_items));

            if (JSON.parse(localStorage.getItem("cartQty"))) {
                var existing_qty = JSON.parse(localStorage.getItem("cartQty"));
                var new_qty = existing_qty + this.qty;
                localStorage.setItem('cartQty', new_qty);
            } else {
                localStorage.setItem('cartQty', this.qty);
            }

            location.reload();
        }
    },
}
</script>
