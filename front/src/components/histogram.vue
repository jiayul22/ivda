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
        <h3>Distribution of Price in Zurich</h3>
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

    <div v-show="isBerlin && isP">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price in Berlin</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="berlin_price"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=600
          />
        </div>
      </div>
    </div>

    <div v-show="isCopenhagen && isP">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price in Copenhagen</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="copenhagen_price"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=1000
          />
        </div>
      </div>
    </div>

    <div v-show="isOslo && isP">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price in Oslo</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="oslo_price"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=1000
          />
        </div>
      </div>
    </div>

    <div v-show="isParis && isP">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price in Paris</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="paris_price"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=1000
          />
        </div>
      </div>
    </div>

    <div v-show="isRome && isP">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price in Rome</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="rome_price"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=1000
          />
        </div>
      </div>
    </div>

    <div v-show="isSanFrancisco && isP">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price in San Francisco</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="SF_price"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=1200
          />
        </div>
      </div>
    </div>

    <div v-show="isStockholm && isP">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Price in Stockholm</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="stockholm_price"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=1000
          />
        </div>
      </div>
    </div>


    <div v-show="(isZurich && isRT)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Room Type in Zurich</h3>
      </v-row>
      <zurich_RT/>
    </div>

    <div v-show="(isBerlin && isRT)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Room Type in Berlin</h3>
      </v-row>
      <berlin_RT/>
    </div>

    <div v-show="(isCopenhagen && isRT)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Room Type in Copenhagen</h3>
      </v-row>
      <copenhagen_RT/>
    </div>

    <div v-show="(isOslo && isRT)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Room Type in Oslo</h3>
      </v-row>
      <oslo_RT/>
    </div>

    <div v-show="(isParis && isRT)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Room Type in Paris</h3>
      </v-row>
      <paris_RT/>
    </div>

    <div v-show="(isRome && isRT)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Room Type in Rome</h3>
      </v-row>
      <rome_RT/>
    </div>

    <div v-show="(isSanFrancisco && isRT)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Room Type in San Francisco</h3>
      </v-row>
      <SF_RT/>
    </div>

    <div v-show="(isStockholm && isRT)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Room Type in Stockholm</h3>
      </v-row>
      <stockholm_RT/>
    </div>


    <div v-show="(isZurich && isMN)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Minimum Nights in Zurich</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="zurich_mn"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=35
          />
        </div>
      </div>
    </div>

    <div v-show="(isBerlin && isMN)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Minimum Nights in Berlin</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="berlin_mn"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=35
          />
        </div>
      </div>
    </div>

    <div v-show="(isCopenhagen && isMN)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Minimum Nights in Copenhagen</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="copenhagen_mn"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=35
          />
        </div>
      </div>
    </div>

    <div v-show="(isOslo && isMN)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Minimum Nights in Oslo</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="oslo_mn"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=35
          />
        </div>
      </div>
    </div>

    <div v-show="(isParis && isMN)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Minimum Nights in Paris</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="paris_mn"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=365
          />
        </div>
      </div>
    </div>

    <div v-show="(isRome && isMN)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Minimum Nights in Rome</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="rome_mn"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=35
          />
        </div>
      </div>
    </div>

    <div v-show="(isSanFrancisco && isMN)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Minimum Nights in San Francisco</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="SF_mn"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=400
          />
        </div>
      </div>
    </div>

    <div v-show="(isStockholm && isMN)">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of Minimum Nights in Stockholm</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data="stockholm_mn"
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0
          :max=35
          />
        </div>
      </div>
    </div>
  </v-card>
</template>

<script>
import zurich_price from "./price/zurichP.json";
import berlin_price from "./price/berlinP.json";
import copenhagen_price from "./price/copenhagenP.json";
import oslo_price from "./price/osloP.json";
import paris_price from "./price/parisP.json";
import rome_price from "./price/romeP.json";
import SF_price from "./price/SFP.json";
import stockholm_price from "./price/stockholmP.json";

import zurich_RT from './roomtypeVue/zurichRT.vue';
import berlin_RT from "./roomtypeVue/berlinRT.vue";
import copenhagen_RT from "./roomtypeVue/copenhagenRT.vue";
import oslo_RT from "./roomtypeVue/osloRT.vue";
import paris_RT from "./roomtypeVue/parisRT.vue";
import rome_RT from "./roomtypeVue/romeRT.vue";
import SF_RT from "./roomtypeVue/SFRT.vue";
import stockholm_RT from "./roomtypeVue/stockholmRT.vue";

import zurich_mn from "./mn/zurichMN.json";
import berlin_mn from "./mn/berlinMN.json";
import copenhagen_mn from "./mn/copenhagenMN.json";
import oslo_mn from "./mn/osloMN.json";
import paris_mn from "./mn/parisMN.json";
import rome_mn from "./mn/romeMN.json";
import SF_mn from "./mn/SFMN.json";
import stockholm_mn from "./mn/stockholmMN.json";

export default {
  name: "App",
  components: {zurich_RT, berlin_RT, copenhagen_RT, oslo_RT, paris_RT, rome_RT, SF_RT, stockholm_RT},

  data:() => ({
    zurich_price: zurich_price,
    berlin_price: berlin_price,
    copenhagen_price: copenhagen_price,
    oslo_price: oslo_price,
    paris_price: paris_price,
    rome_price: rome_price,
    SF_price: SF_price,
    stockholm_price: stockholm_price,

    zurich_RT: zurich_RT,
    berlin_RT: berlin_RT,
    copenhagen_RT: copenhagen_RT,
    oslo_RT: oslo_RT,
    paris_RT: paris_RT,
    rome_RT: rome_RT,
    SF_RT: SF_RT,
    stockholm_RT: stockholm_RT,

    zurich_mn: zurich_mn,
    berlin_mn: berlin_mn,
    copenhagen_mn: copenhagen_mn,
    oslo_mn: oslo_mn,
    paris_mn: paris_mn,
    rome_mn: rome_mn,
    SF_mn: SF_mn,
    stockholm_mn: stockholm_mn,

    city: ['Zurich', 'Berlin', 'Copenhagen', 'Oslo', 'Paris', 'Rome', 'San Francisco', 'Stockholm'],
    feature: ['Price', 'room type', 'minimum nights'],
    selectedCity: 'Select',
    selectedFeature: 'Select',
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