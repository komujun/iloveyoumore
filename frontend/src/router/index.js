import Vue from 'vue';
import VueRouter from 'vue-router';
import Mdb from '@/views/FileUploadMdb';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Mdb',
    component: Mdb,
  },
  {
    path: '/result',
    name: 'result',
    component: () => import('@/views/Result'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
