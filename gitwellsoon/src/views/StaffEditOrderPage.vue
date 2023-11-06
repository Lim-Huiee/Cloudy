<template>

    <div class="container-fluid">
            <h1>
                Edit Order
            </h1>

            <div class="container">
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon3">Order ID</span>
                    </div>
                    <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3" :value="formFields.oid" readonly disabled>
                </div>
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon3">Email</span>
                    </div>
                    <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3" :value="formFields.email" readonly disabled>
                </div>
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon3">Product ID</span>
                    </div>
                    <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3" :value="formFields.pid" readonly disabled>
                </div>
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon3">Quantity</span>
                    </div>
                    <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3" :value="formFields.quantity" readonly disabled>
                </div>

                <div class="row input-field mt-2">
                    <label for="pcat">Status: </label>
                    <select class="form-select" aria-label="Default select example" v-model="formFields.status">
                        <option value="New">New</option>
                        <option value="Processing">Processing</option>
                        <option value="Completed">Completed</option>
                        <option value="Cancelled">Cancelled</option>
                    </select>
                </div>
            </div>

            <div class="container">
                <div class="input-btn-grp">
                    <button class="btn btn-secondary mx-2" onclick="history.back()">
                        <span>Back </span>
                    </button>
                    <button class="btn btn-success mx-2" @click="editOrderStatus()">
                        <span>Save </span>
                        <i class="bi bi-save2"></i>
                    </button>
                </div>
            </div>
        </div>

</template>
<script>
import { getTransitionRawChildren } from "vue";
import { mapActions, mapGetters, mapMutations } from "vuex";

export default {
    name: "StaffOrderPage",
    components: {
    },
    data() {
        return {
            formFields: {
                oid: "",
                email: "",
                pid: "",
                quantity: "",
                status: ""
            },
        }
    },
    async mounted(){
        this.formFields = JSON.parse(localStorage.getItem("editOrderDetails"));
        console.log(this.formFields);
    },
    computed: {
        ...mapGetters(['orders']),
    },
    methods: {
        ...mapActions(['getAllOrders', 'updateOrder']),
        ...mapMutations(),
        async editOrderStatus(details) {
            let res = await this.updateOrder(this.formFields);
            if (res.code == 200) {
                this.$router.push('/StaffOrderPage');
            } else {
                alert("Please try again.")
            }
        }
    }
}
</script>

<style scoped>

.mainPageTitle{
    height: 80px;
    color: #000;
    font-size: 2em;
    font-weight: 600;
    text-align: center;
    border-bottom:1px solid #7d7d7d;
}

th{
    background-color: '#1C3C7C';
    color: white;
    text-align: center;
}

td{
    text-align: 'center';
}

tr:nth-child(even) td {
    background: #EEEEEE;
}

</style>