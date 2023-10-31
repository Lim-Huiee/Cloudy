<template>
    <div class="container-fluid justify-content-center">
        <div class="card mt-5">
            <div style="border-radius:200px; height:200px; width:200px; background: #F8FAF5; margin:0 auto;">
                <i class="checkmark">✓</i>
            </div>
            <h1>Success</h1> 
            <p>We received your purchase request;<br/> we'll be in touch shortly!</p>
        </div>

        <p id="refresh-timer"  class="mt-5"></p>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default {
    name: "PaymentSuccessPage",
    components: {
    },
    data(){
        return {
        }
    },
    async mounted() {
       const refreshTimer = document.getElementById('refresh-timer');

        let timerInSeconds = 5;

        setInterval(() => {
        timerInSeconds -= 1;

        refreshTimer.innerHTML = `Refreshing page in: ${timerInSeconds} seconds`;

        if (timerInSeconds == 0) {
            window.location.href = '/';
        }
        }, 1000);
    },
    computed: {
    },
    methods: {
    },
}
</script>

<style scoped>
body {
    text-align: center;
    padding: 40px 0;
    background: #EBF0F5;
}
h1 {
    color: #88B04B;
    font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
    font-weight: 900;
    font-size: 40px;
    margin-bottom: 10px;
}
p {
    color: #404F5E;
    font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
    font-size:20px;
    margin: 0;
}
i {
color: #9ABC66;
font-size: 100px;
line-height: 200px;
margin-left:-15px;
}
.card {
background: white;
padding: 60px;
border-radius: 4px;
box-shadow: 0 2px 3px #C8D0D8;
display: inline-block;
margin: 0 auto;
}
</style>