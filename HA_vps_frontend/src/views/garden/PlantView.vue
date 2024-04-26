<template>
    
    <div>
        <fwb-card href="#">           
            <div class="p-5 w-35">        
                <img class="scale-50" src="../../assets/icons/plant.png" alt="">     
                <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
                {{ plant.name }}
                </h5>
                <fwb-badge> {{ plant.location }} </fwb-badge>
                <fwb-badge> {{ plant.type }} </fwb-badge>

                <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Sow months:
                    </div>
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    {{ plant_notes.sow_months }}
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Planting method:
                    </div>
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    {{ plant_notes.planting_method }}
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Date planted:
                    </div>
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    {{ plant_notes.date_planted }}
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Soil mix:
                    </div>
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    {{ plant_notes.soil }}
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Container:
                    </div>
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    {{ plant_notes.container }}
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Ideal spacing:
                    </div>
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    {{ plant_notes.ideal_spacing }}
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        # planted:
                    </div>
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    {{ plant_notes.no_planted }}
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Germination time:
                    </div>
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    {{ plant_notes.germination_time }}
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Harvest time:
                    </div>
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    {{ plant_notes.harvest_time }}
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2">
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                        Comment:
                    </div>
                    <div class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    {{ plant_notes.comment }}
                    </div>
                
                 </div>
            </div>
        </fwb-card>
    </div>
    <div class="my-10 p-10 bg-white rounded">
        <fwb-timeline class="vp-raw">
            <div v-for="data in usr_datas">
                <fwb-timeline-item>
                    <fwb-timeline-point>
                        <CalendarDaysIcon class="h-10 w-10"/>
                    </fwb-timeline-point>
                    <fwb-timeline-content>
                        <fwb-timeline-time>
                        {{ data.date }}
                        </fwb-timeline-time>
                        <fwb-timeline-title>
                            <div v-if="data.fertilizer == ''|| data.fertilizer == null"> No Data</div>
                            <div v-else> {{ data.fertilizer }}</div>
                        </fwb-timeline-title>
                        <fwb-timeline-body>
                            <div v-if="data.notes == null || data.notes == ''"> No Notes</div>
                            <div v-else> {{ data.notes }}</div>
                        <!-- {{ data.notes }} -->
                        </fwb-timeline-body>
                    </fwb-timeline-content>
                </fwb-timeline-item>
            </div>
        </fwb-timeline>
    </div>
</template>

<script setup>
    import { useRoute } from 'vue-router'
    import {
        FwbCard,
        FwbBadge,
        FwbTimeline,
        FwbTimelineBody,
        FwbTimelineContent,
        FwbTimelineItem,
        FwbTimelinePoint,
        FwbTimelineTime,
        FwbTimelineTitle,
        } from 'flowbite-vue'
    import { CalendarDaysIcon } from '@heroicons/vue/24/outline'
    
</script>

<script>
    import axios from 'axios'
    import { months, locations } from '../../js/constants.js'

    export default {
        data() {
            return{
                loading: false,
                error: null,
                plant_notes: { },
                plant : { },
                usr_datas: [],
                route: useRoute()
            }
        },
        mounted() {
        this.fetchPlants();
        },
        methods: {
            fetchPlants() {
            this.loading = true;
            axios.get('/garden/plant=' + this.route.params.id)
                .then(response => {
                    console.log('Response', response.data)
                this.loading = false
                this.plant = response.data.plant
                this.plant_notes = JSON.parse(this.plant.description)
                this.usr_datas = response.data.usr_data
                console.log('Response', this.plant_notes)
                console.log('Response', response.data)
                })
                .catch(error => {
                this.loading = false;
                this.error = error.message;
                });
            }
        }
    }
</script>