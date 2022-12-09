<template>
  <v-card height="520">
      <v-combobox
        v-model="selectedCity"
        :items=city
        label="City"
        filled
        height=5
        @change="sendSelectionToBackend($event)"
      ></v-combobox>

      <v-combobox
        v-model="selectedFeature"
        :items=feature
        label="Feature"
        filled
        height=5
        @change="sendSelectionToBackend($event)"
      ></v-combobox>

    <div>{{ typeof this.outData}}</div>
    <div v-show="isHistogram">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of {{selectedFeature}} in {{selectedCity}}</h3>
      </v-row>
      <div style="height: 50vh">
        <div id="app">
          <HistogramSlider
          :width="500"
          :bar-height="200"
          :data=this.outData
          :drag-interval="true"
          :force-edges="true"
          :colors="['#4facfe', '#00f2fe']"
          :min=0

          />
        </div>
      </div>
    </div>

    <div v-show="!isHistogram" id='room_type' style="height:350px; width:90%; margin: auto; text-align: center;">
      <v-row align="center" justify="center" class="mt-0 mb-0">
        <h3>Distribution of {{selectedFeature}} in {{selectedCity}}</h3>
      </v-row>
      <bar/>
    </div>

  </v-card>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
import bar from './roomtypeVue/zurichRT.vue';


export default {
  name: "App",
  components: {bar},

  data:() => ({
    city: ['Zurich', 'Berlin', 'Copenhagen', 'Oslo', 'Paris', 'Rome', 'San Francisco', 'Stockholm'],
    feature: ['Price', 'Room Type', 'Minimum Nights'],
    selectedCity: 'Select',
    selectedFeature: 'Select',
    plotID : 0,
    inputFeature:{
      'city':'',
      'feature':''
    },
    outData : []
  }),

  mounted() {
  },

  methods: {
    async sendSelectionToBackend () {
      this.barPlotId += 1
      this.inputFeature['city'] = this.selectedCity
      this.inputFeature['feature'] = this.selectedFeature
      // construct request
      var paras = ''
      for (const [key, value] of Object.entries(this.inputFeature)) {
        paras = paras+key+'='+value+'&'
      }
      var reqUrl = 'http://127.0.0.1:5000/house?'+paras
      console.log("ReqURL " + reqUrl)

      // await response
      const response = await fetch(reqUrl);
      let res = await response.json();

      if (this.selectedFeature === 'Price' || this.selectedFeature === "Minimum Nights") {
        let out = res.out;
        out.forEach(element => parseFloat(element));
        this.outData = out;
        this.max = res.max;
      }
      else {
        this.outData = res;
      }
    },
    drawLinePlot() {
      const data = [this.outData];
      const layout = {
        // remove the layout of title
      };
      const config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('copenhagen_RT', data, layout, config);
    }
  },

  computed: {
    isHistogram() {
      if ( this.selectedFeature === 'Price' || this.selectedFeature === 'minimum nights'){
        return true;
      } else {
        return false;
      }
    }
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
  padding-top: 30px;
  margin: 0 auto;
  width: 500px;
}

.select.v-text-field.v-text-field--enclosed:not(.v-text-field--rounded)>.v-input__control>.v-input__slot {
  padding-right: 0px
}
</style>