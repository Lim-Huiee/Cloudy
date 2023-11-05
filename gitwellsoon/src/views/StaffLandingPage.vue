<template>

    <div class="container">
        <h1 class="pt-4 mb-4 fw-bolder mainPageTitle">Products List</h1>
        <div class="row">
                <div>
                    <div class="btn-group" role="group" aria-label="Basic example">
                        <router-link to="/StaffSettingPageAdd" class="nav-link text-decoration-none">
                            <button type="button" class="btn btn-success" @click="attachModalData('New')">Add</button>
                        </router-link>
                        <router-link to="/stafforderPage" class="nav-link text-decoration-none mx-5">
                            <button type="button" class="btn btn-success">Go to order page</button>
                        </router-link>
                    </div>
                </div>
                <table class="table mt-3">
                    <tbody>
                        <tr>
                            <th>Product ID</th>
                            <th>Name</th>
                            <th>Category</th>
                            <th>Description</th>
                            <th>Price</th>
                            <th>Img Src</th>
                            <th>Stock</th>
                            <th>Production date</th>
                            <th>Expiry date</th>
                            <th>Edit</th>
                            <th>Delete</th>
                        </tr>
                        <tr v-for="(each, index) in this.products" :key="each">
                            <th scope="row">{{ each.pid }}</th>
                            <td>{{ each.pname }}</td>
                            <td>{{ each.pcat }}</td>
                            <td>{{ each.pdesc }}</td>
                            <td>{{ each.pprice }}</td>
                            <td>{{ each.img_src }}</td>
                            <td>{{ each.stock }}</td>
                            <td>{{ each.prod_date }}</td>
                            <td>{{ each.expiry_date }}</td>
                            <td><button type="btn btn-success" @click="editProduct(each)">Edit</button></td>
                            <td><button type="btn btn-success" @click="removeProduct(each)">Delete</button></td>
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
    name: "SettingsPage",
    components: {
    },
    data() {
        return {
            modalData: {},
        }
    },
    async mounted(){
        await this.getAllProducts();
    },
    computed: {
        ...mapGetters(['products']),
    },
    methods: {
        ...mapActions(['getAllProducts', 'deleteProduct']),
        ...mapMutations(),
        attachModalData(action, data) {
            this.modalData['action'] = action;
            this.modalData['data'] = data;
            console.log(this.modalData);
        },
        editProduct(details) {
            localStorage.setItem("editProductDetails", JSON.stringify(details));
            this.$router.push('/editProduct');
        },
        async removeProduct(details) {
            console.log(details)
            await this.deleteProduct(details);
            location.reload();
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