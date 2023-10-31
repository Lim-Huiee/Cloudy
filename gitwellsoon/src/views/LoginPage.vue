
<template>
  <authenticator>
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

