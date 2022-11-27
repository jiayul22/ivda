<template>
  <v-card height="520">
    <v-list-item
      v-for="(item, i) in selectCategory"
      :key="i"
    >
      <v-combobox
        :items="item.value"
        :label=item.name
        filled
        height=5
        @change="onChange($event,item.name)"
      ></v-combobox>
    </v-list-item>

    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h3>Distribution of Price</h3>
    </v-row>

    <div style="height: 50vh">
      <div id="app">
        <HistogramSlider
        :width="500"
        :bar-height="300"
        :data="price"
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
import zurich from "./price_data/zurich.json";

export default {
  name: "App",

  data:() => ({
    price: zurich,
    inputFeature:{
      'City':'',
    },
    selectCategory:[{
      name: 'Feature', value: ['Price', 'Room Type', 'Minimum nights']
    }]
  }),

  methods: {
      async sendSelectionToBackend () {
        var paras = ''
        for (const [key, value] of Object.entries(this.inputFeature)) {
          console.log('输出',key, value);
          paras = paras+key+'='+value+'&'
        }
        console.log("参数" + paras)
        var reqUrl = 'http://127.0.0.1:5000/PredictPrice?'+paras
        console.log("ReqURL " + reqUrl)

        // await response and data
        const response = await fetch(reqUrl)
        const responseData = await response.json();
        console.log("responseData " + responseData )
      },

      onChange(value,name){
        //
        console.log('输入：',name, value);
        this.inputFeature[name] = value;
      }
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