<template>
  <v-card height="420">

    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h3>Price Prediction</h3>
    </v-row>

    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h1> xxx </h1>
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
