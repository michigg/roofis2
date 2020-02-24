<template>
    <b-row class="h-100">
        <b-col cols="12" class="mt-3 shadow bg-secondary py-3 px-4">
            <h1>Raumauswahl</h1>
            <b-form-row>
                <b-col cols="12" md="8" class="mb-2">
                    <label for="startdate">{{$t('roofisForm.dateLabel')}}</label>
                    <b-input-group size="md">
                        <b-input-group-prepend is-text>
                            <b-icon-calendar font-scale="1.5"></b-icon-calendar>
                        </b-input-group-prepend>
                        <b-form-input id="startdate" type="date" v-model="startDate" required></b-form-input>
                    </b-input-group>
                </b-col>
                <b-col cols="12" md="4" class="mb-2">
                    <label for="starttime">{{$t('roofisForm.timeLabel')}}</label>
                    <b-input-group size="md">
                        <b-input-group-prepend is-text>
                            <b-icon-clock font-scale="1.5"></b-icon-clock>
                        </b-input-group-prepend>
                        <b-form-input id="starttime" type="time" v-model="startTime" required></b-form-input>
                    </b-input-group>
                </b-col>
                <b-col cols="12" sm="6" md="8" class="mb-2">
                    <label for="location-select">{{$t('roofisForm.locationLabel')}}</label>
                    <b-input-group size="md">
                        <b-input-group-prepend is-text>
                            <b-icon-geo font-scale="1.5"></b-icon-geo>
                        </b-input-group-prepend>
                        <b-form-select v-model="selectedBuildingKey" :options="buildingKeys"></b-form-select>
                    </b-input-group>
                </b-col>
                <b-col cols="12" sm="6" md="4" class="mb-2 mt-auto">
                    <b-input-group size="md">
                        <b-button variant="primary" v-on:click="loadPositionRankedBuildings" squared
                                  class="w-100 form-buttom">
                            <b-iconstack font-scale="1" class="mb-1">
                                <b-icon stacked icon="geo" scale="0.4" shift-v="0.9" shift-h="-0.9"></b-icon>
                                <b-icon stacked icon="search"></b-icon>
                            </b-iconstack>
                            {{$t('roofisForm.locationAutoPosition')}}
                        </b-button>
                    </b-input-group>
                </b-col>
                <b-col cols="12" class="mb-2">
                    <label for="min_room_size">{{$t('roofisForm.sizeLabel')}}</label>
                    <b-input-group size="md">
                        <b-input-group-prepend is-text>
                            <b-iconstack font-scale="1.5">
                                <b-icon stacked icon="box-arrow-up-right" scale="0.6" shift-v="0.5" shift-h="0.5"></b-icon>
                                <b-icon stacked icon="square"></b-icon>
                            </b-iconstack>
                        </b-input-group-prepend>
                        <b-form-input id="min_room_size" type="number" v-model="min_size" min="0" step="1"
                                      placeholder="--"></b-form-input>
                        <!--                        <b-form-spinbutton id="min_room_size" wrap min="1" placeholder="&#45;&#45;" v-model="form.min_size"></b-form-spinbutton>-->
                    </b-input-group>
                </b-col>
                <b-col cols="12" class="text-center mt-2">
                    <b-button variant="primary" v-on:click="loadFreeRooms" squared class="btn btn-primary w-75">
                        {{$t('roofisForm.executeSearch')}}
                    </b-button>
                </b-col>
            </b-form-row>
        </b-col>
    </b-row>
</template>

<script>
    export default {
        name: "ParameterSelection",
        data: function () {
            return {
                startDate: null,
                startTime: null,
                buildingKeys: [],
                selectedBuildingKey: null,
                min_size: null,
            }
        },
        mounted() {
            this.initBuildingKeys();
            this.initDate();
            this.initTime();
        },
        methods: {
            initBuildingKeys: function () {
                this.axios
                    .get(this.$data.LECTOR_BUILDING_API)
                    .then((response) => {
                        this.buildingKeys = response.data;
                        this.addSelectDefaultOption();
                    });
            },
            initDate: function () {
                let today = new Date();
                let month = (today.getMonth() + 1).toString();
                if (month.length == 1) {
                    month = "0" + month
                }
                let day = today.getDate().toString();
                if (day.length == 1) {
                    day = "0" + day
                }

                this.startDate = today.getFullYear() + '-' + month + '-' + day;
            },
            initTime: function () {
                let today = new Date();
                let minutes = today.getMinutes();
                let hours = today.getHours();
                if (minutes >= 30) {
                    hours += 1;
                    if (hours > 24) {
                        hours = 0;
                    }
                }
                minutes = 0;
                this.startTime = ("0" + hours).slice(-2) + ":" + ("0" + minutes).slice(-2);
            },
            geo_success(position) {
                let positionFilteredUrl = this.$data.LECTOR_BUILDING_API + "/?coord=" + position.coords.longitude + "," + position.coords.latitude;
                this.axios
                    .get(positionFilteredUrl)
                    .then((response) => {
                        this.buildingKeys = response.data;
                        if (response.data.length > 0) {
                            this.selectedBuildingKey = response.data[0];
                        }
                        this.addSelectDefaultOption();
                    });
            },
            geo_error(error) {
                switch (error.code) {
                    case error.PERMISSION_DENIED:
                        alert("User denied the request for Geolocation.");
                        break;
                    case error.POSITION_UNAVAILABLE:
                        alert("Location information is unavailable.");
                        break;
                    case error.TIMEOUT:
                        alert("The request to get user location timed out.");
                        break;
                    case error.UNKNOWN_ERROR:
                        alert("An unknown error occurred.");
                        break;
                }
            },
            loadPositionRankedBuildings: function () {
                let options = {
                    enableHighAccuracy: true,
                    timeout: Infinity,
                    maximumAge: 30000
                };
                navigator.geolocation.getCurrentPosition(this.geo_success, this.geo_error, options);
            },
            loadFreeRooms: function () {
                let url = this.$data.ROOFIS_API;
                let params = "?start_date=".concat(this.startDate).concat("&start_time=").concat(this.startTime);
                if (this.selectedBuildingKey) {
                    params = params.concat("&building_key=").concat(this.selectedBuildingKey)
                }
                if (this.min_size) {
                    params = params.concat("&min_size=").concat(this.min_size)
                }
                this.axios
                    .get(url.concat(params))
                    .then((response) => {
                        this.$emit('roomsLoaded', response.data)
                    });
            },
            addSelectDefaultOption: function () {
                this.buildingKeys.unshift({value: null, text: this.$t('roofisForm.defaultLocationOption')})
            }
        }
    }
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style scoped>
    .form-buttom {
        height: calc(2.25rem + 2px);
    }
    .row.display-flex {
        display: flex;
        flex-wrap: wrap;
    }
    .row.display-flex > [class*='col-'] {
        display: flex;
        flex-direction: column;
    }

</style>