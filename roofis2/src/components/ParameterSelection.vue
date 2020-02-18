<template>
    <div class="row justify-content-center">
        <div class="col-12 col-xs-11 col-sm-10 col-md-9 col-lg-7 col-xl-5 mt-3 shadow bg-secondary py-3 px-4">
            <form action="/" method="POST">
                <div class="form-row">
                    <div class="col-12 col-md-8 mb-2">
                        <label for="startdate">Wann?</label>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <div class="input-group-text"><i class="far fa-calendar-alt"></i></div>
                            </div>
                            <input type="date"
                                   name="start_date"
                                   class="form-control"
                                   id="startdate"
                                   :value="form.start_date"
                                   placeholder="Datum"
                                   required
                            >
                        </div>
                    </div>
                    <div class="col-12 col-md-4 mb-2">
                        <label for="starttime">Ab</label>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <div class="input-group-text"><i class="far fa-clock"></i></div>
                            </div>
                            <input type="time"
                                   name="start_time"
                                   class="form-control"
                                   id="starttime"
                                   :value="form.start_time"
                                   placeholder="Uhrzeit"
                                   required
                            >
                        </div>
                    </div>
                    <div class="col-12 col-sm-6 col-md-8">
                        <label for="building_key">Wo?</label>
                        <div class="input-group mb-2">
                            <div class="input-group-prepend">
                                <div class="input-group-text"><i class="fas fa-map-marker-alt"></i></div>
                            </div>
                            <select id="location-select" class="custom-select" name="location">
                            </select>
                        </div>
                    </div>
                    <div class="col-12 col-sm-6 col-md-4 mb-2 mt-auto">
                        <div class="input-group">
                            {# TODO: Implement#}
                            <button type="button" onclick="loadPositionRankedBuildings()" id="position-btn"
                                    class="btn btn-primary form-control"
                                    :data-lector-building-api="lector_building_api">
                                <i class="fas fa-search-location"></i> Aktuelle Position
                            </button>
                        </div>
                    </div>
                    <div class="col-12 mb-2">
                        <label for="min_room_size">Für?</label>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <div class="input-group-text"><i class="fas fa-greater-than-equal"></i></div>
                            </div>
                            <input type="number"
                                   name="min_size"
                                   step="1"
                                   class="form-control"
                                   id="min_room_size"
                                   :value="form.min_size"
                                   placeholder="Mindestraumgröße">
                        </div>
                    </div>
                    <div class="col-12 text-center mt-2">
                        <button type="submit" class="btn btn-primary w-75">Raumsuche starten</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ParameterSelection"
    }
</script>

<style scoped>

</style>