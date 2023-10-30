
<template>
  <main>
    <TheWelcome />
  </main>
  <authenticator />

</template>

<script>
import TheWelcome from '../components/TheWelcome.vue'
import {Authenticator} from "@aws-amplify/ui-vue";
import { defineComponent } from 'vue';

export default defineComponent({
  name: "Home",
  components: {
    TheWelcome,
    Authenticator
  },
});

</script>

