<template>
    <b-row v-if="this.openings" class="justify-content-center h-100">
        <b-col cols="12" class="mt-3 shadow bg-secondary py-3 px-4">
            <h2>{{$t('infoBox.headline')}}</h2>
            <b-alert variant="warning" show>
                <i18n path="infoBox.contentInformation" tag="small">
                    <template v-slot:link>
                        <a :href="source" target="_blank">{{ $t('infoBox.contentInformationLinkText') }}</a>
                    </template>
                </i18n>
            </b-alert>

            <b-button v-b-toggle.openings-collapse :aria-expanded="showOpenings ? 'true' : 'false'" variant="primary"
                      class="rounded-0 w-100 d-md-none">
                <span class="when-opened">{{$t('infoBox.hideOpeningsBtnLabel')}}</span>
                <span class="when-closed">{{$t('infoBox.showOpeningsBtnLabel')}}</span>
            </b-button>
            <b-collapse id="openings-collapse" class="mt-2" v-model="showOpenings">
                <table class="table text-left table-sm">
                    <thead>
                    <tr>
                        <th>{{$t('infoBox.tableHeadingLocation')}}</th>
                        <th>{{$t('infoBox.tableHeadingWeekdays')}}</th>
                        <th>{{$t('infoBox.tableHeadingTimes')}}</th>
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
            <h2>{{$t('infoBox.headline')}}</h2>
            <div v-if="!error">
                <p>{{$t('loading')}}</p>
                <b-spinner variant="primary" type="grow" label="Spinning"
                           style="width: 4rem; height: 4rem;"></b-spinner>
            </div>
            <b-alert v-else variant="danger" show>
                {{$t('infoBox.loadingError')}}
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
                error: false,
                showOpenings: true,
            }
        },
        mounted() {
            let url = this.$data.UNI_INFO_API.concat('openings/');

            window.addEventListener('resize', this.onResize);
            this.axios
                .get(url)
                .then((response) => {
                    this.openings = response.data.openings;
                    this.source = response.data.source;
                    this.error = false;
                })
                .catch((error) => {
                    // handle error
                    console.log(error);
                    this.error = true
                })
                .then(function () {
                    // always executed
                });

        },
        methods: {
            onResize: function () {
                this.showOpenings = window.innerWidth >= 768;
            }
        },
        created() {
            this.onResize()
        },
        beforeDestroy: function () {
            window.removeEventListener('resize', this.onResize)
        }
    }
</script>

<style scoped>
    .collapsed > .when-opened,
    :not(.collapsed) > .when-closed {
        display: none;
    }
</style>