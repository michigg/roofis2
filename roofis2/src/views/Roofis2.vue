<template>
    <div class="container-fluid">
        <b-row v-if="this.$data.UNI_INFO_API" class="justify-content-center">
            <b-col cols="12" md="12" lg="9" xl="7" class="mx-1">
                <parameter-selection @roomsLoaded="onRoomsLoaded"></parameter-selection>
            </b-col>
            <b-col cols="12" md="12" lg="9" xl="4" class="mx-1">
                <info-box></info-box>
            </b-col>
        </b-row>
        <b-row v-if="!this.$data.UNI_INFO_API" class="justify-content-center">
            <b-col cols="12" md="12" lg="9" xl="7">
                <parameter-selection @roomsLoaded="onRoomsLoaded"></parameter-selection>
            </b-col>
        </b-row>
        <b-row class="justify-content-center">
            <b-col cols="12" md="12" lg="9" xl="7">
                <results :rooms.sync="this.rooms"></results>
            </b-col>
        </b-row>
    </div>
</template>

<script>
    import ParameterSelection from "../components/ParameterSelection";
    import Results from "../components/Results";
    import InfoBox from "../components/InfoBox";

    export default {
        name: 'Roofis2',
        components: {InfoBox, ParameterSelection, Results},
        data() {
            return {
                rooms: null,
            }
        },
        methods: {
            onRoomsLoaded: function (freeRooms) {
                this.rooms = freeRooms;
                this.$emit('update:rooms', freeRooms)
            }
        },
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .col {
        display: flex;
        flex-flow: column;
    }

    .col .content {
        flex-grow: 1;
    }
</style>
