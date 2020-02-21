<template>
    <nav class="navbar navbar-light bg-secondary">
        <a class="navbar-brand" href="/">RooFiS - Room Finder Service</a>
        <b-navbar-nav class="ml-auto">
            <b-nav-form>
                <b-form-select v-model="$i18n.locale" :options="langs" class="rounded-0 bg-secondary border-dark"></b-form-select>
            </b-nav-form>
        </b-navbar-nav>
    </nav>
</template>

<script>
    export default {
        name: "NavigationBar",
        data() {
            return {
                langs: this.$locales,
            }
        },
    }
</script>

<style scoped>

</style>