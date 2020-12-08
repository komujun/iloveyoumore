import '@fortawesome/fontawesome-free/css/all.min.css';
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbvue/lib/css/mdb.min.css';
import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import router from './router';
import firebase from 'firebase';

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');

Vue.use(VueRouter);

var firebaseConfig = {
  apiKey: 'AIzaSyDAIe0Aq4AeExBCjs653p2YJRAnpSCtpMA',
  authDomain: 'vue-you-279005.firebaseapp.com',
  databaseURL: 'https://vue-you-279005.firebaseio.com',
  projectId: 'vue-you-279005',
  storageBucket: 'vue-you-279005.appspot.com',
  messagingSenderId: '856826690854',
  appId: '1:856826690854:web:20b25cc10daa878c2615e7',
  measurementId: 'G-BG2K5W73DX',
};
firebase.initializeApp(firebaseConfig);
