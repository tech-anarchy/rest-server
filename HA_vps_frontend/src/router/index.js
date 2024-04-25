import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import GardenView from '@/views/garden/GardenView.vue'
import PlantView from '@/views/garden/PlantView.vue'

import AquariumView from '@/views/aqua/AquariumView.vue'

import Temp1View from '@/views/temp/Temp1View.vue'
import Temp2View from '@/views/temp/Temp2View.vue'
import Temp3View from '@/views/temp/Temp3View.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/garden',
      name: 'garden',
      component: GardenView
    },
    {
      path: '/garden/plant/:id',
      name: 'plant',
      component: PlantView
    },
    {
      path: '/aqua',
      name: 'aqua',
      component: AquariumView
    },
    {
      path: '/temp/1',
      name: 'temp1',
      component: Temp1View
    },
    {
      path: '/temp/2',
      name: 'temp2',
      component: Temp2View
    },
    {
      path: '/temp/3',
      name: 'temp',
      component: Temp3View
    }
  ]
})

export default router
