<template>
    <div>
      <h1>Tank View</h1>
      <div v-if="loading">Loading...</div>
      <div v-else>
        <div v-if="error" class="error">Error: {{ error }}</div>
        <div v-else>
            <div class="flex flex-wrap justify-around">

              <div class="w-1/4 px-3 py-3" v-for="tank in tanks" :key="tank.id">
                
                <RouterLink :to="{name: 'plant', params: {id: tank.uuid}}">
                  <fwb-card href="#">
                        
                    <div class="p-5 w-35">        
                        <img class="scale-50" src="../../assets/icons/fish_11792940.png" alt="">     
                        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
                        {{ tank.name }}
                        </h5>
                        <!-- <fwb-badge> {{ plant.location }} </fwb-badge> -->
                        <p class="font-normal text-gray-700 dark:text-gray-400">
                        {{ tank.description }}
                        </p>
                    </div>

                  </fwb-card>
                </RouterLink>

              </div>
              </div>

        </div>
      </div>
    </div>
  </template>

<script setup>
import { 
   FwbCard,
   FwbBadge,
   FwbSpinner,
   FwbImg,
  } from 'flowbite-vue'
</script>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        loading: false,
        error: null,
        tanks: []
      };
    },
    mounted() {
      this.fetchTanks();
    },
    methods: {
      fetchTanks() {
        this.loading = true;
        axios.get('/aqua/')
          .then(response => {
            this.loading = false;
            this.tanks = response.data;
          })
          .catch(error => {
            this.loading = false;
            this.error = error.message;
          });
      }
    }
  }
  </script>
  
  <style>
  .error {
    color: red;
  }
  </style>