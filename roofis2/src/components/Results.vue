<template>
    <div v-if="rooms && rooms.length > 0" class="row justify-content-center mb-5">
        <b-col cols="12" xs="11" sm="10" md="9" lg="7" xl="5" class="mt-3 shadow bg-secondary py-3 px-4">
            <h1 class="text-center">{{$t('results.results')}}</h1>
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
                    <div class="text-left">{{data.value}}</div>
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
    <div v-else-if="rooms && rooms.length == 0" class="row justify-content-center">
        <b-col cols="12" xs="11" sm="10" md="9" lg="7" xl="5" class="mt-3 shadow bg-secondary py-3 px-4 text-center">
            <h1>{{$t('results.results')}}</h1>
            <p>{{$t('results.noFreePlaces')}}</p>
        </b-col>
    </div>
    <div v-else>
    </div>
</template>

<script>
    export default {
        name: "Results",
        props: ["rooms"],
        data() {
            return {
                fields: [{key: 'short', sortable: true},
                    {key: 'name', sortable: true},
                    {key: 'size', sortable: true},
                    {key: 'next_allocation', sortable: true}],
                sortBy: 'short',
                sortDesc: false,
            }
        }
    }
</script>

<style scoped>

</style>