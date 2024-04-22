<template>
    <div class="p-15 bg-white border border-gray-200 rounded-lg">
        <form action="" class="space-y-6" v-on:submit.prevent="submitPlant">
            <div>
                <label for="">Plant*</label><br>
                <input type="plant" v-model="form.plant" placeholder="Plant Name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
            </div>
            <div>
                <label for="">Location*</label><br>
                <input type="location" v-model="form.location" placeholder="Location" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
            </div>
            <div>
                <label for="">Type</label><br>
                <input type="type" placeholder="Months to sow" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
            </div>
            <div>
                <label for="">Months to sow</label><br>
                <input type="sow_mon" v-model="notes.sow_month" placeholder="Months to sow" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
            </div>
            <div>
                <label for="">Seed/Plant</label><br>
                <input type="seed_plant" placeholder="Seed/Plant" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
            </div>
            <div>
                <label for="">Date Planted</label><br>
                <input type="day_plnt" placeholder="Date Planted" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
            </div>
            <div>
                <label for="">Ideal Spacing</label><br>
                <input type="spacing" placeholder="Date Planted" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
            </div>
            <div>
                <label for="">Where Planted</label><br>
                <input type="plant_container" placeholder="Container (size) or Ground" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
            </div>
            <div>
                <label for="">Soil Mix</label><br>
                <input type="location" placeholder="Container (size) or Ground" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
            </div>
            <div>
                <label for="">Germination Time</label><br>
                <input type="ger_time" placeholder="Container (size) or Ground" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
            </div>
            <div>
                <label for="">Harvest Time</label><br>
                <input type="har_time" placeholder="Container (size) or Ground" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
            </div>
            <div>
                <label for="">Comments</label><br>
                <input type="comment" v-model="notes.comment" placeholder="Container (size) or Ground" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
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
                notes: {
                        sow_month : '',
                        comment: ''
                    },
                form : {
                    plant: '',
                    location: '',
                    description: ''
                },
                errors: [],
            }
        },

        methods : {
            submitPlant() {
                this.errors = []
                this.form.description = JSON.stringify(this.notes)
                
                if (this.form.plant === '') {
                    this.errors.push('No Plant Name Provided')
                }

                if (this.form.location === '') {
                    this.errors.push('No Location Provided')
                }

                if (this.errors.length === 0) {
                    axios
                    .post('/garden/plants/post/', this.form)
                    .then( response => {
                        console.log('info', response.data)
                    }
                    )
                }
            }
        }
    }
</script>