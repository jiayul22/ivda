<template>
    <main>
        <div id='SF_RT' style="height:350px; width:90%; margin: auto; text-align: center;"></div>
    </main>
  </template>

  <script>
  import Plotly from 'plotly.js/dist/plotly';

  export default {
    data: () => ({
        SF_RT_data: {x: ['Entire home/apt', 'Private room', 'Hotel room', 'Shared room'], y: [4243, 2221, 65, 82]},
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
            x: this.SF_RT_data.x,
            y: this.SF_RT_data.y,
            type: 'bar'
          };
          var data = [trace1];
          var layout = {
            // remove the layout of title

          };
          var config = {responsive: true, displayModeBar: false}
          Plotly.newPlot('SF_RT', data, layout, config);
      }
    }
  }
  </script>

  <style scoped>
  </style>