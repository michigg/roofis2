<template>
    <div v-if="results" class="row justify-content-center mb-5">
        <div class="col-12 col-xs-11 col-sm-10 col-md-9 col-lg-7 col-xl-5 mt-3 shadow bg-secondary py-3 px-4">
            <h1 class="text-center">Ergebnisse</h1>
            <table id="results" class="table table-striped table-bordered" cellspacing="0" style="width:100%">
                <thead>
                <tr>
                    <th>#</th>
                    <th>Raum <i class="fas fa-cube"></i></th>
                    <th>Typ <i class="fas fa-shapes"></i></th>
                    <th>Plätze <i class="fas fa-chair"></i></th>
                    <th>Frei <i class="fas fa-stopwatch"></i></th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="room in this.freeRooms" :key="room">
                    <td>{{ loop.index }}</td>
                    <td>
                        <a :href="lector_url/room.building_key/room.floor/room.number">{{ room }}</a>
                    </td>
                    <td>{{ room.name }}</td>
                    <td>{{ room.size }}</td>
                    <td class="text-center">
                        {% if room.next_allocation %}
                        bis {{ room.next_allocation }}
                        {% else %}
                        <i class="fas fa-check text-success"></i>
                        {% endif %}
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div v-else class="row justify-content-center">
        <div class="col-12 col-xs-11 col-sm-10 col-md-9 col-lg-7 col-xl-5 mt-3 shadow bg-secondary py-3 px-4 text-center">
            <h1>Ergebnisse</h1>
            <p>Keine Freien Räume gefunden</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Results",
        computed: {
            freeRooms: function () {
                return this.rooms.filter((room) => room.building_key && room.floor && room.number)
            }
        }
    }
</script>

<style scoped>

</style>