<template>
  <v-card height="260">
    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h3>Map??</h3>
    </v-row>
  </v-card>
</template>

<script>
export default {

  name: "LinePlot",
  props: ["selectedCompany", "selectedAlgorithm"],

  data: () => ({
    LinePlotData: {x: [], y: []}
  }),
  
}
</script>

<style scoped>

</style>
