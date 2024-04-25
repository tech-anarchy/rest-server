<template>
  <div class="py-10 px-8 border-b border-gray-200">
      <div class="p-15 bg-white border border-gray-200 rounded-lg justify-center">
          <div v-if="b_showPlantForm">
              <form action="" class="space-y-6" v-on:submit.prevent="closeForm">
                  <fwb-button class="m-5" color="purple" outline square>
                      <XMarkIcon class="w-5 h-5 hover:white"/>
                  </fwb-button>
              </form>
              <form action="" class="space-y-6 justify-center" v-on:submit.prevent="submitPlant">
                  <div class="container py-5 px-5 grid grid-row-5 gap-4 justify-center">
                      <div class="py-5 grid grid-cols-1 sm:grid-cols-2 gap-4">
                          <div v-if="b_plantName">
                              <fwb-input
                                  v-model="plant_form.plant"
                                  placeholder="Plant Name"
                                  label="Plant"
                              />
                          </div>
                          <div v-else>
                              <fwb-input
                                  v-model="plant_form.plant"
                                  placeholder="Plant Name"
                                  label="Plant"
                                  validation-status="error"
                              />
                          </div>
                          <div v-if="b_plantLocation">
                              <fwb-select
                                  v-model="plant_form.location"
                                  :options="locations"
                                  label="Select a location"
                              />
                          </div>
                          <div v-else>
                              <fwb-select
                                  v-model="plant_form.location"
                                  :options="locations"
                                  label="Select a location"
                                  validation-status="error"
                              />
                          </div>
                      </div>

                      <div>
                          <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                              Months to sow:
                          </label>
                          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                              <div v-for="month in months" :key="month">
                                  <input v-model="plant_notes.sow_months" :value="month" class="mr-2 leading-tight" type="checkbox">
                                  <span class="text-sm">{{ month }}</span>
                              </div>
                          </div>
                      </div>

                      <div class="py-5 grid grid-cols-1 sm:grid-cols-2 gap-4">
                          
                          <div>
                              <label for="time" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Date Sown:</label>
                              <vue-tailwind-datepicker v-model="plant_notes.date_planted" :formatter="formatter" as-single/>
                          </div>
                          <div>
                              <fwb-input
                                  v-model="plant_notes.planting_method"
                                  placeholder="Seed/Plant"
                                  label="Seed/Plant"
                              />
                          </div>
                          <div>
                              <fwb-input
                                  v-model="plant_notes.soil"
                                  placeholder="Soil Mix"
                                  label="Soil Mix"
                              />
                          </div>
                          <div>
                              <fwb-input
                                  v-model="plant_notes.container"
                                  placeholder="Container(size)"
                                  label="Container(size)"
                              />
                          </div>
                          <div>
                              <fwb-input
                                  v-model="plant_notes.ideal_spacing"
                                  placeholder="Ideal Spacing"
                                  label="Ideal Spacing"
                              />
                          </div>
                          <div>
                              <fwb-input
                                  v-model="plant_notes.no_planted"
                                  placeholder="# of seeds/saplings"
                                  label="Nos. in container"
                              />
                          </div>
                          <div>
                              <fwb-input
                                  v-model="plant_notes.germination_time"
                                  placeholder="Germination Time"
                                  label="Germination Time"
                              />
                          </div>
                          <div>
                              <fwb-input
                                  v-model="plant_notes.harvest_time"
                                  placeholder="Harvest Time"
                                  label="Harvest Time"
                              />
                          </div>
                      </div>
                      <div class="py-5">
                          <fwb-textarea
                              v-model="plant_notes.comment"
                              :rows="4"
                              label="Comments"
                              placeholder="Write your message..."
                          />
                      </div>

                      <div class="py-5">
                          <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Submit</button>
                      </div>
                  </div>
              </form>
          </div>
          <div v-else-if="b_showFertilizerForm">
              <form action="" class="space-y-6" v-on:submit.prevent="closeForm">
                  <fwb-button class="m-5" color="purple" outline square>
                      <XMarkIcon class="w-5 h-5 hover:white"/>
                  </fwb-button>
              </form>

              <form action="" class="space-y-6 justify-center" v-on:submit.prevent="submitFertilizer">
                  <div class="container py-5 px-5 grid grid-row-3 gap-4 justify-center">
                      <div class="py-5 grid grid-cols-1 sm:grid-cols-2 gap-4">
                          <div v-if="b_fertilizeruser">
                              <fwb-input
                                  v-model="fertilizer_form.user"
                                  placeholder="username"
                                  label="username"
                              />
                          </div>
                          <div v-else>
                              <fwb-input
                                  v-model="fertilizer_form.user"
                                  placeholder="username"
                                  label="username"
                                  validation-status="error"
                              />
                          </div>
                          <div v-if="b_fertilizerData">
                              <fwb-input
                                  v-model="fertilizer_form.fertilizer"
                                  placeholder="Fertilizer/Pesticide"
                                  label="Fertilizer"
                              />
                          </div>
                          <div v-else>
                              <fwb-input
                                  v-model="fertilizer_form.fertilizer"
                                  placeholder="Fertilizer/Pesticide"
                                  label="Fertilizer"
                                  validation-status="error"
                              />
                              <label class="block mb-2 text-sm font-medium text-red-500 dark:text-white">
                                  Either note or fertilizer/pesticide required.
                              </label>
                          </div>
                          <div>
                              <div v-if="b_fertilizerDate">
                                  <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                      Date:
                                  </label>
                              </div>
                              <div v-else>
                                  <label class="block mb-2 text-sm font-medium text-red-700 dark:text-white">
                                      Date:
                                  </label>
                              </div>
                              <vue-tailwind-datepicker v-model="fertilizer_form.date" :formatter="formatter" as-single/>
                          </div>
                      </div>

                      <div>
                          <div v-if="b_fertilizerPlants">
                              <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                  Select Plants:
                              </label>
                              <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                                  <div v-for="plant in plants" :key="plant.uuid">
                                      <input v-model="fertilizer_form.plants" :value="plant.uuid" class="mr-2 leading-tight" type="checkbox">
                                      <span class="text-sm">{{ plant.name }} - {{ getLocation(plant.location)}}</span>
                                  </div>
                              </div>
                          </div>
                          <div v-else>
                              <label class="block mb-2 text-sm font-medium text-red-700 dark:text-white">
                                  Select Plants:
                              </label>
                              <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                                  <div v-for="plant in plants" :key="plant.uuid">
                                      <input v-model="fertilizer_form.plants" :value="plant.uuid" class="mr-2 leading-tight" type="checkbox">
                                      <span class="text-sm text-red-500">{{ plant.name }} - {{ getLocation(plant.location)}} </span>
                                  </div>
                              </div>
                          </div>
                      </div>

                      <div class="py-5" v-if="b_fertilizerData">
                          <fwb-textarea
                              v-model="fertilizer_form.comments"
                              :rows="4"
                              label="Notes"
                              placeholder="Write your message..."
                          />
                      </div>
                      <div v-else>
                          <fwb-textarea
                              v-model="fertilizer_form.comments"
                              :rows="4"
                              label="Notes"
                              placeholder="Write your message..."
                          />
                          <label class="block mb-2 text-sm font-medium text-red-500 dark:text-white">
                              Either note or fertilizer/pesticide required.
                          </label>
                      </div>

                      <div class="py-5">
                          <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Submit</button>
                      </div>

                  </div>
              </form>
          </div>

          <div class="m-5 flex justify-center" v-else>
              <div>
                  <form action="" class="mx-5 space-y-6" v-on:submit.prevent="showPlantForm">
                      <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Add New Plant</button>
                  </form>
              </div>
              <div>
                  <form action="" class="mx-5 space-y-6" v-on:submit.prevent="showFertilizerForm">
                      <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Update Fertilizer</button>
                  </form>
              </div>
              
          </div>
      </div>

    <div v-if="loading"><fwb-spinner /></div>
    <div v-else>
      <div v-if="error" class="error">Error: {{ error }}</div>
      <div class="container mx-auto px-4 py-10" v-else>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">

          <div v-for="plant in plants" :key="plant.id">
            
            <RouterLink :to="{name: 'plant', params: {id: plant.uuid}}">
              <fwb-card href="#">
                    
                <div class="p-5 w-35">        
                    <img class="scale-50" src="../../assets/icons/plant.png" alt="">     
                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
                    {{ plant.name }}
                    </h5>
                    <fwb-badge> {{ getLocation(plant.location)}} </fwb-badge>
                    <div class="my-3" v-for="temp in [parseDescription(plant.description)]">

                      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            Sow months:
                        </div>
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                          {{ temp.sow_months }}
                        </div>
                      </div>

                      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            Planting method:
                        </div>
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                          {{ temp.planting_method }}
                        </div>
                      </div>

                      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            Date planted:
                        </div>
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                          {{ temp.date_planted[0] }}
                        </div>
                      </div>

                      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            Soil mix:
                        </div>
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                          {{ temp.soil }}
                        </div>
                      </div>

                      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            Container:
                        </div>
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                          {{ temp.container }}
                        </div>
                      </div>

                      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            Ideal spacing:
                        </div>
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                          {{ temp.ideal_spacing }}
                        </div>
                      </div>

                      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            # planted:
                        </div>
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                          {{ temp.no_planted }}
                        </div>
                      </div>

                      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            Germination time:
                        </div>
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                          {{ temp.germination_time }}
                        </div>
                      </div>

                      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            Harvest time:
                        </div>
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                          {{ temp.harvest_time }}
                        </div>
                      </div>

                      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                            Comment:
                        </div>
                        <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                          {{ temp.comment }}
                        </div>
                      </div>
                      
                    </div>
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
  import { MapPinIcon } from '@heroicons/vue/24/solid'
  import { CalendarDaysIcon,
          XMarkIcon } from '@heroicons/vue/24/solid'
  import { 
     FwbCard,
     FwbBadge,
     FwbSpinner,
     FwbInput,
     FwbTextarea,
     FwbButton,
     FwbSelect
  } from 'flowbite-vue'

  import { ref } from "vue";
  import VueTailwindDatepicker from "vue-tailwind-datepicker"


  const formatter = ref({
  date: 'DD-MMM-YYYY',
  month: 'MMM',
  })
</script>

<script>
  import axios from 'axios'
import { months, locations } from '../../js/constants.js'

export default {
data() {
    return {
        
        loading: false,
        error: null,
        plants: [],

        desc_notes: {},

        b_plantName: true,
        b_plantLocation: true,

        b_submitPlantForm: true,

        b_showPlantForm: false,

        b_fertilizeruser: true,
        b_fertilizerDate: true,
        b_fertilizerPlants: true,
        b_fertilizerData: true,

        b_submitFertilizerForm: true,

        b_showFertilizerForm: false,
        
        plant_notes: {
            sow_months : ref([]),
            planting_method: '',
            date_planted : ref([]),
            soil: '',
            container : '',
            ideal_spacing: '',
            no_planted: '',
            germination_time: '',
            harvest_time: '',
            comment: ''
        },
        plant_form : {
            plant: '',
            location: '',
            description: ''
        },


        fertilizer_form : {
            user : '',
            fertilizer : '',
            date: ref([]),
            plants : [],
            comments : ''
        },
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
    getLocation(locationKey) {
    const plantLocation = locations.find(location => location.value === locationKey);
    return plantLocation.name
    },
    parseDescription(desc) {
    const plantNotes = JSON.parse(desc)
    return plantNotes
    // this.desc_notes = plantNotes
    },
    submitPlant() {
            this.b_submitPlantForm = true
            this.b_plantLocation = true
            this.b_plantName = true
            this.errors = []
            this.plant_form.description = JSON.stringify(this.plant_notes)
            if (this.plant_form.plant === ''){
                this.b_plantName = false
                this.b_submitPlantForm = false
            }
            if (this.plant_form.location === ''){
                this.b_plantLocation = false
                this.b_submitPlantForm = false
            }
            if (this.b_submitPlantForm) {
                console.log('info', this.plant_form)

                axios
                .post('/garden/plants/post/', this.plant_form)
                .then( response => {
                    console.log('info', response.data)
                }
                )

                this.resetForm()
            }
            
            },
        submitFertilizer() {
            this.b_submitFertilizerForm = true
            this.b_fertilizeruser = true
            this.b_fertilizerPlants = true,
            this.b_fertilizerData = true
            this.b_fertilizerDate = true

            if (this.fertilizer_form.user === '') {
                this.b_fertilizeruser = false
                this.b_submitFertilizerForm = false
            }
            if (this.fertilizer_form.plants.length === 0) {
                this.b_fertilizerPlants = false
                this.b_submitFertilizerForm = false
            }
            if (this.fertilizer_form.fertilizer === '' && this.fertilizer_form.comments === ''){
                this.b_fertilizerData = false
                this.b_submitFertilizerForm = false
            }
            if (this.fertilizer_form.date.length === 0){
                this.b_fertilizerDate = false
                this.b_submitFertilizerForm = false
            }
            if (this.b_submitFertilizerForm){
                console.log('Selected Objects:', this.fertilizer_form)

                axios
                .post('/garden/fertilizers/post/', this.fertilizer_form)
                .then( response => {
                    console.log('info', response.data)
                }
                )

                this.resetForm()
            }
            
        },

        showPlantForm() {
            this.b_showPlantForm = true
        },
        showFertilizerForm() {
            this.b_showFertilizerForm = true
        },
        closeForm() {
            this.b_showPlantForm = false
            this.b_showFertilizerForm = false

            this.resetForm()
        },

        resetForm() {
            this.b_plantName = true
            this.b_plantLocation = true

            this.b_submitPlantForm = true

            this.b_showPlantForm = false

            this.b_fertilizeruser = true
            this.b_fertilizerDate = true
            this.b_fertilizerPlants = true
            this.b_fertilizerData = true

            this.b_submitFertilizerForm = true

            this.b_showFertilizerForm = false
            
            this.plant_notes.sow_months = ref([])
            this.plant_notes.planting_method = ''
            this.plant_notes.date_planted = ref([])
            this.plant_notes.soil = ''
            this.plant_notes.container = ''
            this.plant_notes.ideal_spacing = ''
            this.plant_notes.no_planted = ''
            this.plant_notes.germination_time = ''
            this.plant_notes.harvest_time = ''
            this.plant_notes.comment = ''

            this.plant_form.plant = ''
            this.plant_form.location = ''
            this.plant_form.description = ''


            this.fertilizer_form.user = ''
            this.fertilizer_form.fertilizer = ''
            this.fertilizer_form.date = ref([])
            this.fertilizer_form.plants = []
            this.fertilizer_form.comments = ''
        }
}
}
</script>
  
  <style>
  .error {
    color: red;
  }
  </style>