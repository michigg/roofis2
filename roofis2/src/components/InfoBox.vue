<template>
    <b-row v-if="this.openings" class="justify-content-center h-100">
        <b-col cols="12" class="mt-3 shadow bg-secondary py-3 px-4">
            <h2>Öffnungszeiten:</h2>
            <b-alert variant="warning" show><small>Diese Daten werden direkt von der <a :href="source">Webseite</a>
                gelesen und können daher fehlerhaft sein.</small></b-alert>

            <b-button v-b-toggle.openings-collapse :aria-expanded="showOpenings ? 'true' : 'false'" variant="primary"
                      class="rounded-0 w-100">
                <span class="when-opened">Öffnungszeiten ausblenden</span>
                <span class="when-closed">Öffnungszeite anzeigen</span>
            </b-button>
            <b-collapse id="openings-collapse" class="mt-2" v-model="showOpenings">
                <table class="table text-left table-sm">
                    <thead>
                    <tr>
                        <th>Ort</th>
                        <th>Wochentage</th>
                        <th>Uhrzeit</th>
                    </tr>
                    </thead>
                    <tr v-for="opening in openings" :key="opening.location">
                        <td>{{opening.location}}</td>
                        <td>{{opening.start_weekday}} - {{opening.end_weekday}}</td>
                        <td> {{opening.start_time}} -
                            {{opening.end_time}}
                        </td>
                    </tr>
                </table>
            </b-collapse>
        </b-col>
    </b-row>
    <b-row v-else-if="!this.openings && this.$data.UNI_INFO_API" class="justify-content-center h-100">
        <b-col cols="12" class="mt-3 shadow bg-secondary py-3 px-4">
            <h2>Öffnungszeiten:</h2>
            <div v-if="!error">
                <p>Lade...</p>
                <b-spinner variant="primary" type="grow" label="Spinning"
                           style="width: 4rem; height: 4rem;"></b-spinner>
            </div>
            <b-alert v-else variant="danger" show>
                {{error}}
            </b-alert>
        </b-col>
    </b-row>

</template>

<script>
    export default {
        name: "InfoBox",
        data() {
            return {
                openings: null,
                source: "",
                error: null,
                showOpenings: true,
            }
        },
        mounted() {
            let url = this.$data.UNI_INFO_API.concat('openings/');
            if (window.innerWidth < 768) {
                this.showOpenings = false;
            }
            this.axios
                .get(url)
                .then((response) => {
                    this.openings = response.data.openings;
                    this.source = response.data.source;
                    this.error = null;
                })
                .catch((error) => {
                    // handle error
                    console.log(error);
                    this.error = "Es konnten keine Öffnungszeiten geladen werden";
                })
                .then(function () {
                    // always executed
                });

        }
    }
</script>

<style scoped>
    .collapsed > .when-opened,
    :not(.collapsed) > .when-closed {
        display: none;
    }
</style>