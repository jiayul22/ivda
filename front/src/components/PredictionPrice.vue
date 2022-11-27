<template>

  <main>
    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h3>Price Prediction</h3>
    </v-row>

    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h1 class="green--text"> {{ $props.price }}</h1>
    </v-row>

    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h3>Neighborhood Avg</h3>
    </v-row>

    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h1 class="green--text"> {{ $props.neighborhood_avg }}</h1>
    </v-row>

    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h3>Name Score</h3>
    </v-row>

    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h1 class="green--text"> {{ $props.name_score }}</h1>
    </v-row>


  </main>


</template>

<script>
export default {

  name: "PredictionPrice",
  props: ["price", "neighborhood_avg", 'name_score'],

  data: () => ({
    LinePlotData: {x: [], y: []}
  }),

  mounted() {
    this.print()
  },

  methods: {
    print() {
        console.log("!!price predict: " , this.$props.price);
    }
  }
  
}
</script>

<style scoped>

</style>
