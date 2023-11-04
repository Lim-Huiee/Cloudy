
<template>
  <authenticator class="mt-5">
    <template v-slot = "{user, signOut}">
      <button @click="signOut">Sign Out</button>
    </template>
  </authenticator>
</template>

<script>
import TheWelcome from '../components/TheWelcome.vue'
import {Authenticator} from "@aws-amplify/ui-vue";
import { defineComponent } from 'vue';

export default defineComponent({
  name: "Login",
  components: {
    TheWelcome,
    Authenticator
  },
});

</script>


 <!-- <template>
  <div class="vue-tempalte">
      <form @submit.prevent="register">
          <h3>Sign Up</h3>

          <div class="form-group">
              <label>Email address</label>
              <input type="email" v-model="email" class="form-control form-control-lg" />
          </div>

          <div class="form-group">
              <label>Password</label>
              <input type="password" v-model="password" class="form-control form-control-lg" />
          </div>
          <button type="submit" style="margin-top: 10px;" class="btn btn-dark btn-lg btn-block">Sign Up</button>
      </form>
  </div>
</template>

<script>
import { Auth } from 'aws-amplify';

export default {
  name: 'Register',
  data() {
      return {
          email: '',
          password: '',
      };
  },
  methods: {
      async register() {
          try {
              await Auth.signUp({
                  username: this.email,
                  password: this.password,
              });
              alert('User successfully registered. Please login');
          } catch (error) {
              alert(error.message);
          }
      },
  },
};
</script> -->
