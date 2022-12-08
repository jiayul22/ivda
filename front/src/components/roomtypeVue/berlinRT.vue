<template>
    <main>
        <div id='berlin_RT' style="height:350px; width:90%; margin: auto; text-align: center;"></div>
    </main>
  </template>

  <script>
  import Plotly from 'plotly.js/dist/plotly';

  export default {
    data: () => ({
        berlin_RT_data: {x: ['Entire home/apt', 'Private room', 'Hotel room', 'Shared room'], y: [9904, 6438, 146, 192]},
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
            x: this.berlin_RT_data.x,
            y: this.berlin_RT_data.y,
            type: 'bar'
          };
          var data = [trace1];
          var layout = {
            // remove the layout of title

          };
          var config = {responsive: true, displayModeBar: false}
          Plotly.newPlot('berlin_RT', data, layout, config);
      }
    }
  }
  </script>

  <style scoped>
  </style>