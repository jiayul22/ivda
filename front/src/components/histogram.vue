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
      <v-combobox
        v-model="selectedFeature"
        :items=feature
        label="Feature"
        filled
        height=5
        @change="onChange($event,item.name)"
      ></v-combobox>

    <div v-show="isZurich && isP">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price in Zurch</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
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

    <div v-show="isZurich && isP">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price in Zurch</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
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

    <div v-show="isZurich && isP">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price in Zurch</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
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

    <div v-show="isZurich && isP">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price in Zurch</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
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

    <div v-show="isZurich && isP">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price in Zurch</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
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

    <div v-show="(isZurich && isRT)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Room Type in Zurch</h3>
      </v-row>
      <zurich_RT/>
    </div>

    <div v-show="isOslo">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>test</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
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
import zurich_price from "./price/zurichP.json";
import test from "./test_data/test_price.json";

import zurich_RT from './roomtypeVue/zurichRT.vue';

export default {
  name: "App",
  components: {zurich_RT},

  data:() => ({
    zurich_price: zurich_price,
    zurich_RT: zurich_RT,
    test_price: test,
    city: ['Zurich', 'Berlin', 'Copenhagen', 'Oslo', 'Paris', 'Rome', 'San Francisco', 'Stockholm'],
    feature: ['Price', 'room type', 'minimum nights'],
    selectedCity: 'Select',
    selectedFeature: 'Select',

    LinePlotData: {x: [], y: []},
    testData: {x: ['a', 'b', 'c', 'd'], y: [110, 200, 5, 1111]},
    responseData:{ 'profit': [{'feature': 2021, 'weight': 33364}, {'feature': 2020, 'weight': 21331}, {'feature': 2019, 'weight': 11588}]}
  }),

  computed: {
    isZurich() {
      return this.selectedCity === 'Zurich';
    },
    isBerlin() {
      return this.selectedCity === 'Berlin';
    },
    isCopenhagen() {
      return this.selectedCity === 'Copenhagen';
    },
    isOslo() {
      return this.selectedCity === 'Oslo';
    },
    isParis() {
      return this.selectedCity === 'Paris';
    },
    isRome() {
      return this.selectedCity === 'Rome';
    },
    isSanFrancisco() {
      return this.selectedCity === 'San Francisco';
    },
    isStockholm() {
      return this.selectedCity === 'Stockholm';
    },
    isP() {
      return this.selectedFeature === 'Price';
    },
    isRT() {
      return this.selectedFeature === 'room type';
    },
    isMN() {
      return this.selectedFeature === 'minimum nights';
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
  padding-top: 30px;
  margin: 0 auto;
  width: 500px;
}

.select.v-text-field.v-text-field--enclosed:not(.v-text-field--rounded)>.v-input__control>.v-input__slot {
  padding-right: 0px
}
</style>