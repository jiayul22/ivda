<template>

  <main>
    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h3>Price Prediction</h3>
    </v-row>

    <v-row align="center" justify="center" class="mt-2 mb-0">
      <h1 :class="$props.price > $props.neighborhood_avg? 'green--text' : 'red--text'">  {{ $props.price }}</h1>
    </v-row>

    <v-row align="center" justify="center" class="mt-10 mb-0">
      <h3>Name Score</h3>
    </v-row>

    <v-row align="center" justify="center" class="mt-2 mb-0">
      <h1 :class="$props.name_score > 60? 'green--text' : 'red--text'"> {{ $props.name_score }}</h1>
    </v-row>

    <v-row align="center" justify="center" class="mt-10 mb-0">
      <h3>Neighborhood Avg</h3>
    </v-row>

    <v-row align="center" justify="center" class="mt-2 mb-0">
      <h1 class="blue-grey--text"> {{ $props.neighborhood_avg }}</h1>
    </v-row>

    <v-row
      align="center"
      class="mt-10"
    >
    </v-row>

    <v-row
      align="center"
      class="mt-1"
      no-gutters
      v-for="(indicator, i) in indicators"
      :key="i"
    >
      <v-col
        class="text-no-wrap"
        cols="5"
      >
        <v-chip
          v-if="2"
          :color="indicator.color"
          class="ml-3 mt-5 black--text"
          label
          small
        >
          {{indicator.summary}}
        </v-chip>
      </v-col>

      <v-col
        class="mt-4 ma-0"
        cols="5"
      >
        <h6>{{indicator.text}}</h6>
      </v-col>
    </v-row>

  </main>


</template>

<script>
export default {

  name: "PredictionPrice",
  props: ["price", "neighborhood_avg", 'name_score'],

  data: () => ({
    indicators: [
      {'color':'red lighten-3', 'summary':'Warm' , 'text':'Need Improvement'}, 
      {'color':'green lighten-3', 'summary':'Good', 'text':'Healthy Performance'}
    ],
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
