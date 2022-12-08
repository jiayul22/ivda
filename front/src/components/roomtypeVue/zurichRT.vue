<template>
    <main>
        <div id='myLinePlot' style="height:350px; width:650px; margin: auto;"></div>
    </main>
  </template>

  <script>
  import Plotly from 'plotly.js/dist/plotly';

  export default {
    data: () => ({
        RTdata: {x: ['Entire home/apt', 'Private room', 'Hotel room', 'Shared room'], y: [110, 200, 5, 1111]},
    }),

    mounted() {
      this.fetchData()
    },

    methods: {
      fetchData() {
          // draw the lineplot after the data is transformed
          this.drawLinePlot()
        },
      drawLinePlot() {
          var trace1 = {
            x: this.RTdata.x,
            y: this.RTdata.y,
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