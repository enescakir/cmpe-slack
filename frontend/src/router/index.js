import Vue from 'vue';
import Router from 'vue-router';
import MakeRequest from '@/components/MakeRequest';


Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: MakeRequest,
    },
  ],
});
