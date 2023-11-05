<template>

    <div class="container">
        <h1 class="pt-4 mb-4 fw-bolder mainPageTitle">Orders List</h1>
        <div>
            <div class="btn-group" role="group" aria-label="Basic example">
                <router-link to="/StaffLandingPage" class="nav-link text-decoration-none">
                    <button type="button" class="btn btn-success">Go to product list page</button>
                </router-link>
            </div>
        </div>
        <div class="row">
                <table class="table mt-3">
                    <tbody>
                        <tr>
                            <th>Order ID</th>
                            <th>Email</th>
                            <th>Product ID</th>
                            <th>Quantity</th>
                            <th>Status</th>
                        </tr>
                        <tr v-for="(each, index) in this.orders" :key="each">
                            <td>{{ each.oid }}</td>
                            <td>{{ each.email }}</td>
                            <td>{{ each.pid }}</td>
                            <td>{{ each.quantity }}</td>
                            <td>{{ each.status }}</td>
                            <td><button type="btn btn-success" @click="editOrderStatus(each)">Edit</button></td>
                        </tr>
                    </tbody>
                </table>
        </div>
    </div>
    <SystemSettingsModal :modalData="modalData"/>

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
            modalData: {},
        }
    },
    async mounted(){
        await this.getAllOrders();
    },
    computed: {
        ...mapGetters(['orders']),
    },
    methods: {
        ...mapActions(['getAllOrders']),
        ...mapMutations(),
        editOrderStatus(details) {
            localStorage.setItem("editOrderDetails", JSON.stringify(details));
            this.$router.push('/editOrder');
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