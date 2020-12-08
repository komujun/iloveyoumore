<template>
  <div>
    <div id="nav">
      <app-header></app-header>
      <transition name="fade">
        <Router-view />
      </transition>
    </div>
    <div class="desktop-view">
      <Desktop-view></Desktop-view>
    </div>
  </div>
</template>
<script>
import AppHeader from '@/components/AppHeader.vue';
import DesktopView from './components/DesktopView.vue';
export default {
  components: {
    AppHeader,
    DesktopView,
  },
};
</script>
<style>
@font-face {
  font-family: 'Bazzi';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.1/Bazzi.woff')
    format('woff');
  font-weight: normal;
  font-style: normal;
}
* {
  font-family: 'Bazzi';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.1/Bazzi.woff')
    format('woff');
  font-weight: normal;
  font-style: normal;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav a {
  font-weight: bold;
  color: #eeeeee;
}

#nav a.router-link-exact-active {
  color: #f2009f;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
@media (min-width: 450px) {
  #nav {
    display: none;
  }
}
@media (max-width: 450px) {
  .desktop-view {
    /* visibility: hidden; */
    display: none;
  }
}
</style>
