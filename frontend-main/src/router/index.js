import { createRouter, createWebHistory } from 'vue-router';
import CodeInput from '../components/CodeInput.vue';
import CodeResults from '../components/CodeResults.vue';

const routes = [
  { path: '/', component: CodeInput },
  { path: '/results', component: CodeResults }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
