<template>
  <div class="header">
    <!-- <router-link to="/">마이페이지</router-link> | -->
    <router-link to="/">누가 더 좋아하는지 알아보기</router-link>
  </div>
</template>

<script>
export default {};
</script>

<style>
.header {
  background-color: #f2b3d1;
  color: white;
  padding: 8px 8px 8px 25px;
  display: flex;
  justify-content: center;
  align-items: center;
  -webkit-box-shadow: 0px 5px 10px 0px rgba(0, 0, 0, 0.5);
  -moz-box-shadow: 0px 5px 10px 0px rgba(0, 0, 0, 0.5);
  box-shadow: 0px 5px 10px 0px rgba(0, 0, 0, 0.5);
}
.header a:visited {
  color: white;
}
.header a:active {
  color: #35495e;
}
.fixed {
  position: fixed;
  width: 100%;
  z-index: 999;
}
.logo {
  width: 30px;
  margin-right: 18px;
}
a {
  margin: 0 5px;
}
</style>
