<template>
  <div>
    <top-bar />
    <div>
    <h5>{{ msg }}</h5>
    </div>
  </div>
</template>

<script>
// import axios from 'axios';
import TopBar from './TopBar'

export default {
  components: {
    TopBar
  },
  name: 'Ping',
  data() {
    return {
      msg: 'Hello',
    };
  },
  // methods: {
  //   getMessage() {
  //     axios.get('/recommendations/1')
  //       .then((response) => {
  //         console.log('response from API', response);
  //         this.msg = response.data;
  //       })
  //       .catch((error) => {
  //         console.error(error);
  //       });
  //   },
  // },
  // created() {
  //   this.getMessage();
  // },
};
</script>
