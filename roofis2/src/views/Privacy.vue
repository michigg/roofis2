<template>
  <b-row class="justify-content-center">
    <b-col cols="12" xs="11" sm="10" md="9" lg="7" xl="6" class="mt-3 shadow bg-secondary py-3 px-4">
      <h1>Datenschutz</h1>
      <p v-html="this.$data.PRIVACY_DATA"></p>
    </b-col>
  </b-row>
</template>

<script>
export default {
  name: 'privacy',
}
</script>
