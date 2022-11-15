<template>
  <main>
    <v-row align="center" justify="center" class="mt-0 mb-0">
      <h3>Feature Weight</h3>
    </v-row>

    <div style="height: 50vh">
      <div id='myLinePlot' style="height: inherit"></div>
    </div>

  </main>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';

export default {

  name: "barPlot",
  props: ["weights"],
  data: () => ({
    LinePlotData: {x: [], y: []},
    responseData:{ 'profit': [{'feature': 2021, 'weight': 33364}, {'feature': 2020, 'weight': 21331}, {'feature': 2019, 'weight': 11588}]}
  }),
  
  mounted() {
    this.fetchData()
  },

  methods: {
    fetchData() {
      // transform data to usable by lineplot
      console.log('触发')
      this.$props.weights.forEach((i) => {
        console.log('!!weight: ', i.weight)
        this.LinePlotData.x.push(i.feature)
        this.LinePlotData.y.push(i.weight)
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
