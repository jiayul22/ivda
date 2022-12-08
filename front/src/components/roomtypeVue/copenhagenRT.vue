<template>
    <main>
        <div id='copenhagen_RT' style="height:350px; width:90%; margin: auto; text-align: center;"></div>
    </main>
  </template>

  <script>
  import Plotly from 'plotly.js/dist/plotly';

  export default {
    data: () => ({
        copenhagen_RT_data: {x: ['Entire home/apt', 'Private room', 'Hotel room', 'Shared room'], y: [12230, 1551, 15, 19]},
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
            x: this.copenhagen_RT_data.x,
            y: this.copenhagen_RT_data.y,
            type: 'bar'
          };
          var data = [trace1];
          var layout = {
            // remove the layout of title

          };
          var config = {responsive: true, displayModeBar: false}
          Plotly.newPlot('copenhagen_RT', data, layout, config);
      }
    }
  }
  </script>

  <style scoped>
  </style>