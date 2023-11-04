<!-- 
<template>
  <authenticator class="mt-5">
    <template v-slot = "{user, signOut}">
      <button @click="signOut">Sign Out</button>
    </template>
  </authenticator>
  
</template>

<script>
import StaffLandingPage from './StaffLandingPage.vue';
import TheWelcome from '../components/TheWelcome.vue'
import {Authenticator} from "@aws-amplify/ui-vue";
import { defineComponent } from 'vue';
import { Hub } from 'aws-amplify';

Hub.listen('Authenticator', (data) => {
  switch (data.payload.event) {
    case 'signIn':
        console.log('user signed in');
        break;
  }
});

export default defineComponent({
  name: "Login",
  components: {
    TheWelcome,
    Authenticator
  },
  
});

</script>

 -->

 <template>
  <div class="vue-tempalte">
      <form @submit.prevent="login">
          <h3>Sign In</h3>

          <div class="form-group">
              <label>Email address</label>
              <input type="email" v-model="email" class="form-control form-control-lg" />
          </div>

          <div class="form-group">
              <label>Password</label>
              <input type="password" v-model="password" class="form-control form-control-lg" />
          </div>

          <button type="submit" style="margin-top: 10px;" class="btn btn-dark btn-lg btn-block">Sign In</button>

      </form>
  </div>
</template>
<script>
import { Auth } from 'aws-amplify';
export default {
  name: 'Login',
  data() {
      return {
          email: '',
          password: '',
      };
  },
  methods: {
      async login() {
          try {
              const user = await Auth.signIn(this.email, this.password);
              console.log('user', user);
              alert('Successfully logged in');
              window.location.href = './StaffLandingPage';
          } catch (error) {
              alert(error.message);
          }
      },
  },
};
</script>