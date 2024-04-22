<template>
    <div class="py-10 px-8 border-b border-gray-200">
      <h1>Garden View</h1>
      <div v-if="loading">Loading...</div>
      <div v-else>
        <div v-if="error" class="error">Error: {{ error }}</div>
        <div v-else>
            {{ plants }}
          <!-- <div v-for="plant in plants" :key="plant.id"> -->
            <!-- <h2>{{ plant }}</h2> -->
            <!-- <p>{{ plant.description }}</p> -->
          <!-- </div> -->
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        loading: false,
        error: null,
        plants: []
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
      }
    }
  }
  </script>
  
  <style>
  .error {
    color: red;
  }
  </style>