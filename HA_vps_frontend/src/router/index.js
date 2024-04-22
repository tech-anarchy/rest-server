import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import GardenView from '@/views/garden/GardenView.vue'
import AddPlantView from '@/views/garden/AddPlantView.vue'
import UpdateFertilizerView from '@/views/garden/UpdateFertilizerView.vue'
import PlantView from '@/views/garden/PlantView.vue'

import AquariumView from '@/views/aqua/AquariumView.vue'


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
      path: '/garden//plant/:id',
      name: 'plant',
      component: PlantView
    },
    {
      path: '/garden/addplant',
      name: 'addplant',
      component: AddPlantView
    },
    {
      path: '/garden/addfertilizer',
      name: 'addfertilizer',
      component: UpdateFertilizerView
    },
    {
      path: '/aqua',
      name: 'aqua',
      component: AquariumView
    }
  ]
})

export default router
