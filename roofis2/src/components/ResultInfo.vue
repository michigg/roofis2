<template>
  <b-alert v-if="!this.is_lecture_time" variant="warning" show>
    <i18n path="resultInfo.contentInformation" tag="small">
      <template v-slot:link>
        <a :href="source" target="_blank">{{ $t('resultInfo.contentInformationLinkText') }}</a>
      </template>
    </i18n>
  </b-alert>
  <b-alert v-else-if="this.is_free_day" variant="warning" show>
    <i18n path="resultInfo.freeDayInformation" tag="small">
      <template v-slot:link>
        <a :href="source" target="_blank">{{ $t('resultInfo.freeDayInformationLinkText') }}</a>
      </template>
    </i18n>
  </b-alert>
  <b-alert v-else-if="error && this.$data.UNI_INFO_API" variant="danger" show>
    {{ $t('resultInfo.loadingError') }}
  </b-alert>
</template>

<script>
export default {
  name: "ResultInfo",
  data() {
    return {
      is_free_day: false,
      is_lecture_time: true,
      source: "",
      error: false,
    }
  },
  mounted() {
    let url = this.$data.UNI_INFO_API.concat('info/today/');

    this.axios
        .get(url)
        .then((response) => {
          this.is_free_day = response.data.is_free_day;
          this.is_lecture_time = response.data.is_lecture_day;
          this.source = response.data.source;
          this.error = false;
          console.log(this.is_free_day, this.is_lecture_time)
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
}
</script>
