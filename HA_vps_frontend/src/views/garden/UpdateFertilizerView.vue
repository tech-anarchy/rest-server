<template>
    <div>
      <form @submit.prevent="submitForm">
        <div>
            <label for="">Username*</label><br>
                <input type="username" v-model="form.user" placeholder="Username" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
        </div>
        <div>
            <label for="">Fertilizer*</label><br>
                <input type="fertilizer" v-model="form.fertilizer" placeholder="Fertilizer" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
        </div>
        <div>
            <label for="selectedObjects">Select Objects:</label>
            <select id="selectedObjects" v-model="selectedObjects" multiple>
            <option v-for="plant in plants" :key="plant.uuid" :value="plant.uuid">
                {{ plant.name }}
            </option>
            </select>
        </div>
        
        <div>
                <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Submit</button>
            </div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    data() {
      return {
        loading: false,
        plants: [],
        error: null,
        selectedObjects: [],
        form : {
            user : '',
            fertilizer : '',
            plants : []
        }
      };
    },
    mounted() {
      // Make an HTTP GET request to fetch objects
      this.fetchObjects();
    },
    methods: {
      fetchObjects() {
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
      submitForm() {
        // Do something with selectedObjects
        this.form.plants = this.selectedObjects
        console.log('Selected Objects:', this.form)

        axios
            .post('/garden/fertilizers/post/', this.form)
            .then( response => {
                console.log('info', response.data)
            }
            )
      }
    }
  };
  </script>