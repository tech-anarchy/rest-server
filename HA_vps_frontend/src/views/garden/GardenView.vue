<template>
  <div class="py-10 px-8 border-b border-gray-200">

    <div v-if="loading"><fwb-spinner /></div>
    <div v-else>
      <div v-if="error" class="error">Error: {{ error }}</div>
      <div v-else>
        <div class="flex flex-wrap justify-around">

          <div class="w-1/4 px-3 py-3" v-for="plant in plants" :key="plant.id">
            
            <RouterLink :to="{name: 'plant', params: {id: plant.uuid}}">
              <fwb-card href="#">
                    
                <div class="p-5 w-35">        
                    <img class="scale-50" src="../../assets/icons/plant.png" alt="">     
                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
                    {{ plant.name }}
                    </h5>
                    <fwb-badge> {{ plant.location }} </fwb-badge>
                    <p class="font-normal text-gray-700 dark:text-gray-400">
                    {{ plant.description }}
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
  import axios from 'axios'
  
  export default {
    data() {
      return {
        loading: false,
        error: null,
        plants: [],
      };
    },
    mounted() {
      this.fetchPlants();
    },
    methods: {
      fetchPlants() {
        this.loading = true;
        axios.get('/garden/')
          .then(response => {
            this.loading = false;
            this.plants = response.data;
          })
          .catch(error => {
            this.loading = false;
            this.error = error.message;
          });
      },
    }
  }
  </script>
  
  <style>
  .error {
    color: red;
  }
  </style>