<template>
    <div>
        <div class="container-fluid">
            <div>
                <parameter-selection @roomsLoaded="onRoomsLoaded"></parameter-selection>
                <results :rooms.sync="this.rooms"></results>
            </div>
        </div>
    </div>
</template>

<script>
    import ParameterSelection from "../components/ParameterSelection";
    import Results from "../components/Results";

    export default {
        name: 'Roofis2',
        components: {ParameterSelection, Results},
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
<style scoped>

</style>
