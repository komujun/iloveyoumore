<template>
  <div class="result-page">
    <section class="people">
      <div class="user">
        <img
          :src="crop_image1"
          alt=""
          class="animate__animated animate__rotateIn male p1 "
        />
        <div class="name">{{ p1 }}</div>
      </div>
      <div>{{ sign }}</div>
      <div class="user">
        <img
          :src="crop_image2"
          alt=""
          class="animate__animated animate__rotateIn male p2"
        />
        <div class="name">{{ p2 }}</div>
      </div>
    </section>
    <section>
      <span class="animate__animated animate__fadeInUp">
        {{ data }}
      </span>
    </section>
    <mdb-btn color="deep-orange" class="again-btn" @click="goback"
      >❤❤ 다시하기 ❤❤
    </mdb-btn>
  </div>
</template>

<script>
import { mdbBtn } from 'mdbvue';
import store from '@/store/index';
export default {
  components: {
    mdbBtn,
  },
  data() {
    const { data, crop_image1, crop_image2, sign } = store.state.res;
    const { p1, p2 } = store.state.req;
    return {
      data,
      crop_image1,
      crop_image2,
      sign,
      p1,
      p2,
    };
  },
  methods: {
    goback() {
      this.$router.push('/');
    },
    judge() {
      if (this.sign === '<') {
        const user = document.querySelector('.p2');
        user.style.width = '150px';
        user.style.height = '150px';
        user.classList.add('heartBeat');
      } else if (this.sign === '>') {
        const user = document.querySelector('.p1');
        user.style.width = '150px';
        user.style.height = '150px';
        user.classList.add('heartBeat');
      }
      return 1;
    },
  },
  mounted() {
    this.judge();
  },
};
</script>

<style>
.result-page {
  display: flex;
  flex-direction: column;
}
.people {
  width: 100%;
  display: flex;
  align-items: center;
}
section {
  margin: 60px auto;
  display: flex;
  justify-content: space-around;
}
.user {
  display: flex;
  flex-direction: column;
}
.name {
  margin: auto;
}
.male {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: solid 1px #f2009f;
}
.animate__animated.animate__fadeInUp {
  --animate-duration: 5s;
}
.again-btn {
  font-size: 1rem;
}

@keyframes heartBeat {
  0% {
    transform: scale(1);
  }

  14% {
    transform: scale(1.3);
  }

  28% {
    transform: scale(1);
  }

  42% {
    transform: scale(1.3);
  }

  70% {
    transform: scale(1);
  }
}

.heartBeat {
  animation-name: heartBeat;
  animation-duration: calc(var(--animate-duration) * 3);
  animation-timing-function: ease-in-out;
}
</style>
