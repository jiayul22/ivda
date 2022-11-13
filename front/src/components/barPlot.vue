<template>
  <v-card max-height="420" >
    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h3>Profit View of Company</h3>
    </v-row>

    <div style="height: 50vh">
      <div id='myLinePlot' style="height: inherit"></div>
    </div>

  </v-card>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';

export default {

  name: "LinePlot",

  data: () => ({
    LinePlotData: {x: [], y: []},
    responseData:{ 'profit': [{'year': 2021, 'value': 33364}, {'year': 2020, 'value': 21331}, {'year': 2019, 'value': 11588}, {'year': 2018, 'value': 10073}, {'year': 2017, 'value': 3033}]}
  }),

  mounted() {
    this.fetchData()
  },

  methods: {
    async fetchData() {
      // transform data to usable by lineplot
      this.responseData.profit.forEach((profit) => {
        console.log(profit.year)
        this.LinePlotData.x.push(profit.year)
        this.LinePlotData.y.push(profit.value)
      })

      // draw the lineplot after the data is transformed
      this.drawLinePlot()
    },
    drawLinePlot() {
      var trace1 = {
        x: this.LinePlotData.x,
        y: this.LinePlotData.y,
        type: 'bar'
      };
      var data = [trace1];
      var layout = {
        // remove the layout of title

      };
      var config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('myLinePlot', data, layout, config);
    }
  }

}
</script>

<style scoped>

</style>
