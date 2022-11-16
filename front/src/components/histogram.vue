<template>
  <v-card height="520">
    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h3>Distribution of price in Zurich</h3>
    </v-row>

    <div style="height: 50vh">
      <div id="app">
        <HistogramSlider
        :width="500"
        :bar-height="300"
        :data="data"
        :drag-interval="true"
        :force-edges="true"
        :colors="['#4facfe', '#00f2fe']"
        :min=0
        :max=1200
        />
        </div>
    </div>

  </v-card>
</template>

<script>
import data from "./price_data/zurich.json";

export default {
  name: "App",

  data() {
    return {
      data: data
    };
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding-top: 50px;
  margin: 0 auto;
  width: 500px;
}
</style>