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
        <b-row class="justify-content-center mb-5">
            <b-col cols="12" md="12" lg="9" xl="7">
                <results :rooms.sync="this.rooms"
                         :rooms-error.sync="this.roomsLoadingError"
                         :rooms-loading.sync="this.roomsLoadingState">
                </results>
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
                roomsLoadingError: false,
                roomsLoadingState: false
            }
        },
        methods: {
            onRoomsLoaded: function (data) {
                this.rooms = data.rooms;
                this.roomsLoadingError = data.error;
                this.roomsLoadingState = data.loading;
                this.$emit('update:rooms', this.rooms);
                this.$emit('update:rooms', this.roomsLoadingError);
                this.$emit('update:rooms', this.roomsLoadingError);
            },
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
