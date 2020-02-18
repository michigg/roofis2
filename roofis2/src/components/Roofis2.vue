<template>
    <div>
        <parameter-selection></parameter-selection>
        <results></results>
    </div>
</template>

<script>
    import Results from "./Results";
    import ParameterSelection from "./ParameterSelection";

    export default {
        name: 'Roofis2',
        components: {ParameterSelection, Results},
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h3 {
        margin: 40px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>
