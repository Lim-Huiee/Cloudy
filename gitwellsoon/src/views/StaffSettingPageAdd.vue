<template>
    <div class="position-relative">
        <div class="container-fluid">
            <h1>
                Add New Product
            </h1>

            <form class="container" @submit.prevent="submitForm">
                <div class="row input-field mt-2">
                    <label for="pcat">Product Category:</label>

                    <select name="pcat" id="pcat" v-model="formFields.pcat" >
                        <option value="Bandage">Bandage</option>
                        <option value="Blood Pressure Monitor">Blood Pressure Monitor</option>
                        <option value="Face Mask">Face Mask</option>
                        <option value="First Aid Kit">First Aid Kit</option>
                        <option value="Gloves">Gloves</option>
                        <option value="Hand Sanitizer">Hand Sanitizer</option>
                        <option value="IV drips">IV drips</option>
                        <option value="Support">Support</option>
                        <option value="Ventilator">Ventilator</option>
                        <option value="Wheelchair">Wheelchair</option>
                    </select>
                </div>

                <div class="row input-field mt-2">
                    <label for="pname" class="col-form-label col-sm-2 required">Product Name</label>
                    <div class="col-sm-6">
                        <input v-model="formFields.pname" type="text" class="form-control" id="pname" required>
                    </div>
                </div>

                <div class="row input-field mt-2">
                    <label for="pdesc" class="col-form-label col-sm-2 required">Product Description</label>
                    <div class="col-sm-6">
                        <input v-model="formFields.pdesc" type="text" class="form-control" id="pdesc" required>
                    </div>
                </div>

                <div class="row input-field mt-2">
                    <label for="pprice" class="col-form-label col-sm-2 required">Product Price</label>
                    <div class="col-sm-6">
                        <input v-model="formFields.pprice" type="number" class="form-control" id="pprice" required>
                    </div>
                </div>

                <div class="row input-field mt-2">
                    <label for="stock" class="col-form-label col-sm-2 required">Product Stock</label>
                    <div class="col-sm-6">
                        <input v-model="formFields.stock" type="number" class="form-control" id="stock" required>
                    </div>
                </div>

                <div class="row input-field mt-2">
                    <label for="prod_date" class="col-form-label col-sm-2 required">Product Production Date</label>
                    <div class="col-sm-6">
                        <input v-model="formFields.prod_date" type="text" class="form-control" id="prod_date" placeholder="YYYY-MM-DD" required>
                    </div>
                </div>

                <div class="row input-field mt-2">
                    <label for="expiry_date" class="col-form-label col-sm-2 required">Product Expiry Date</label>
                    <div class="col-sm-6">
                        <input v-model="formFields.expiry_date" type="text" class="form-control" id="expiry_date" placeholder="YYYY-MM-DD" required>
                    </div>
                </div>
                <div class="row input-field mt-2">
                    <label for="img_src" class="col-form-label col-sm-2 required">Product Image</label>
                    <div class="col-sm-6">
                        <input type="file" class="form-control" id="img_src" required @change="handleFileChange">
                    </div>
                </div>
            </form>

            <div class="container">
                <div class="input-btn-grp">
                    <button class="btn btn-secondary mx-2" onclick="history.back()">
                        <span>Back </span>
                    </button>
                    <button class="btn btn-success mx-2" @click="addProduct()">
                        <span>Save </span>
                        <i class="bi bi-save2"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import AWS from './aws-config.js';
import { mapActions, mapMutations, mapGetters } from "vuex";
import Axios from 'axios'; 

export default {
    name: "Add",
    components: {
    },
    data(){
        return{
            formFields: {
                pcat: "",
                pname: "",
                pdesc: "",
                pprice: "",
                img_src: "",
                stock: "",
                prod_date: "",
                expiry_date: "",
            },
            toastrResponse: "",
            loading: false,
            errormsg: [],
            errorString: ""
        };
    },
    async mounted() {
        await this.getAllProducts()
    },
    computed: {
        ...mapGetters(['products'])
    },
    methods: {
        ...mapActions(['getAllProducts', 'createProduct']),
        validateFields(details){

        },
        validateMCR(details) {

        },
        async addProduct(){
            console.log(this.formFields);
            await this.createProduct(this.formFields);

            this.$router.push('/StaffLandingPage');

        },
        async handleFileChange(event) {
            this.addProduct();
            const file = event.target.files[0]; // Get the selected file
            const s3 = new AWS.S3(); // Create an S3 instance

            const params = {
            Bucket: 'gitwellsoon-product', // Replace with your S3 bucket name
            Key: this.formFields['pcat'].replaceAll(' ','') + '_' + this.formFields['pname'].replaceAll(' ','') + '.png' , // Provide a unique key for your object
            Body: file,
            };

            try {
            const data = await s3.upload(params).promise();
            console.log('File uploaded successfully:', data.Location);
            // You can handle the response, e.g., save the S3 URL to your database
            } catch (error) {
            console.error('Error uploading file:', error);
            }
            }   
        },
        async addProduct() {
            console.log(this.formFields);
            

            // Prepare the data to send to the API
            const data = {
                pcat: this.formFields.pcat,
                pname: this.formFields.pname,
                pdesc: this.formFields.pdesc,
                pprice: this.formFields.pprice,
                stock: this.formFields.stock,
                prod_date: this.formFields.prod_date,
                expiry_date: this.formFields.expiry_date,
                img_src: img_src
            };

            // Make an HTTP POST request to your API
            try {
                const response = await Axios.post('http://localhost:5000/create_product', data);
                console.log(response.data);
                // Handle the response, e.g., show a success message or redirect
            } catch (error) {
                console.error('Error creating product:', error);
                // Handle the error, e.g., show an error message
            }
        },
}
</script>