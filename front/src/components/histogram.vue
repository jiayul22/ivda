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
        :prettify="prettify"
        :drag-interval="true"
        :force-edges="true"
        :colors="['#4facfe', '#00f2fe']"
        :min="new Date(2004, 11, 24).valueOf()"
        :max="new Date(2017, 11, 24).valueOf()"
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
      data: data.map(d => new Date(d)),
      prettify: function(ts) {
        return new Date(ts).toLocaleDateString("en", {
          year: "numeric",
          month: "short",
          day: "numeric"
        });
      }
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
  width: 800px;
}
</style>