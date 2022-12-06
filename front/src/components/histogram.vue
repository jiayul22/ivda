<template>
  <v-card height="520">
      <v-combobox
        v-model="selectedCity"
        :items=city
        label="City"
        filled
        height=5
        @change="onChange($event,item.name)"
      ></v-combobox>

    <div v-show="isZurich">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="300"
          :data="zurich_price"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=1200
          />
        </div>
      </div>
    </div>

    <div v-show="isOslo">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>test</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="300"
          :data="test_price"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=120
          />
        </div>
      </div>
    </div>

  </v-card>
</template>

<script>
import zurich_price from "./price_data/zurich.json";
import test from "./test_data/test_price.json";

export default {
  name: "App",

  data:() => ({
    zurich_price: zurich_price,
    test_price: test,
    city: ['Zurich', 'Oslo', 'Berlin'],
    selectedCity: 'Select',
  }),

  computed: {
    isZurich() {
      return this.selectedCity === 'Zurich';
    },
    isOslo() {
      return this.selectedCity === 'Oslo';
    },
    isButton() {
      return this.selectedCity === 3;
    },
  },
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

.select.v-text-field.v-text-field--enclosed:not(.v-text-field--rounded)>.v-input__control>.v-input__slot {
  padding-right: 4px
}
</style>