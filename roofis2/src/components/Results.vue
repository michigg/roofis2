<template>
    <div v-if="rooms && rooms.length > 0 && !roomsLoading" class="row justify-content-center mb-5" data-cy="data-cy=room-result">
        <b-col cols="12" class="mt-3 shadow bg-secondary py-3 px-4">
            <h2 class="text-center">{{$t('results.headline')}}</h2>
            <result-info></result-info>
            <b-table
                    stacked="sm"
                    small
                    sort-icon-right
                    :fields="fields"
                    :items="rooms"
                    :sort-by.sync="sortBy"
                    :sort-desc.sync="sortDesc"
            >
                <template v-slot:head(short)>
                    <div class="text-left">{{$t('results.room')}}
                        <b-icon icon="square" font-scale="1.25"></b-icon>
                    </div>
                </template>
                <template v-slot:head(name)>
                    <div class="text-left">{{$t('results.type')}}
                        <b-icon-columns-gutters font-scale="1.25"></b-icon-columns-gutters>
                    </div>
                </template>
                <template v-slot:head(size)>
                    <div class="text-left">{{$t('results.size')}}
                        <b-iconstack font-scale="1.25">
                            <b-icon stacked icon="box-arrow-up-right" scale="0.6" shift-v="0.5"
                                    shift-h="0.5"></b-icon>
                            <b-icon stacked icon="square"></b-icon>
                        </b-iconstack>
                    </div>
                </template>
                <template v-slot:head(next_allocation)>
                    <div class="text-left">{{$t('results.free')}}
                        <b-icon-clock font-scale="1.25"></b-icon-clock>
                    </div>
                </template>
                <template v-slot:cell(size)="data">
                    <span v-if="data.value===-1">{{$t('results.notAvailable')}}</span>
                    <span v-else>{{data.value}}</span>
                </template>
                <template v-slot:cell(short)="data">
                    <div class="text-left"><a :href="getRoofisLink(data.value)" target="_blank">{{data.value}}</a></div>
                </template>
                <template v-slot:cell(name)="data">
                    <div class="text-left">{{data.value}}</div>
                </template>
                <template v-slot:cell(next_allocation)="data">
                    <span v-if="data.value">{{$t('results.freeUntil')}} {{data.value}}</span>
                    <span v-else><b-icon icon="check" font-scale="1.5" variant="success"></b-icon></span>
                </template>
            </b-table>
        </b-col>
    </div>
    <b-row v-else-if="rooms && rooms.length === 0 && !roomsLoading && !roomsError" class="justify-content-center" data-cy="data-cy=room-result">
        <b-col cols="12" class="mt-3 shadow bg-secondary py-3 px-4">
            <h1>{{$t('results.headline')}}</h1>
            <b-alert variant="warning" show>
                {{$t('results.noFreePlaces')}}
            </b-alert>
        </b-col>
    </b-row>
    <b-row v-else-if="rooms && rooms.length === 0 && roomsLoading" class="justify-content-center" data-cy="data-cy=room-result">
        <b-col cols="12" class="mt-3 shadow bg-secondary py-3 px-4">
            <h2>{{$t('results.headline')}}</h2>
            <p>{{$t('loading')}}</p>
            <b-spinner variant="primary" type="grow" label="Spinning"
                       style="width: 4rem; height: 4rem;"></b-spinner>
        </b-col>
    </b-row>
    <b-row v-else-if="rooms && rooms.length === 0 && roomsError" class="justify-content-center" data-cy="data-cy=room-result">
        <b-col cols="12" class="mt-3 shadow bg-secondary py-3 px-4">
            <h2>{{$t('results.headline')}}</h2>
            <b-alert variant="danger" show>
                {{$t('results.loadingError')}}
            </b-alert>
        </b-col>
    </b-row>
</template>

<script>
    import ResultInfo from "./ResultInfo";

    export default {
        name: "Results",
        components: {ResultInfo},
        props: ["rooms", "roomsLoading", "roomsError"],
        data() {
            return {
                fields: [{key: 'short', sortable: true},
                    {key: 'name', sortable: true},
                    {key: 'size', sortable: true},
                    {key: 'next_allocation', sortable: true}],
                sortBy: 'short',
                sortDesc: false,
                shortMap: {},
            }
        },
        watch: {
            rooms: function (newVal) { // watch it
                this.shortMap = this.resultlistToDict(newVal)
            }
        },
        methods: {
            getRoofisLink: function (roomShort) {
                if (this.shortMap) {
                    let room = this.shortMap[roomShort];
                    return this.$data.LECTOR_WEB_URL + room.building_key + "/" + room.floor + "/" + room.number
                } else {
                    return "#"
                }
            },
            resultlistToDict: function (list) {
                return list.reduce(function (map, obj) {
                    map[obj.short] = obj;
                    return map;
                }, {});
            }
        }
    }
</script>

<style scoped>

</style>
