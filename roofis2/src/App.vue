<template>
    <div id="app">
        <navigation-bar></navigation-bar>
        <b-container fluid class="home">
            <router-view></router-view>
        </b-container>
        <footer class="text-center fixed-bottom bg-secondary">
            <p class="mb-0 mt-1">© Copyright 2020, Michael Götz
                (<a href="/imprint">Impressum</a>,
                <a href="/privacy">Datenschutz</a>)</p>
            <p class="mb-0"><a href="https://github.com/michigg/roofis2/issues" target="_blank">
                <i class="fab fa-github"></i> Problem melden</a><span
                    class="ml-2">Version: {{ this.$data.VERSION }}</span></p>
        </footer>
    </div>
</template>

<script>
    import NavigationBar from "./components/NavigationBar";

    export default {
        name: 'App',
        components: {NavigationBar},
    }
</script>

<style lang="scss">
    @import './assets/styles/custom.scss';
    @import '../node_modules/bootstrap/scss/bootstrap.scss';
    @import '../node_modules/bootstrap-vue/src/index.scss';
</style>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }
</style>
