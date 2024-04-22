<template>
    <div>
      <h1>Tank View</h1>
      <div v-if="loading">Loading...</div>
      <div v-else>
        <div v-if="error" class="error">Error: {{ error }}</div>
        <div v-else>
            {{ tanks }}
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