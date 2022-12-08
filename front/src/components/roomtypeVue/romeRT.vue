<template>
    <main>
        <div id='rome_RT' style="height:350px; width:90%; margin: auto; text-align: center;"></div>
    </main>
  </template>

  <script>
  import Plotly from 'plotly.js/dist/plotly';

  export default {
    data: () => ({
        rome_RT_data: {x: ['Entire home/apt', 'Private room', 'Hotel room', 'Shared room'], y: [16579, 7276, 782, 0]},
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
            x: this.rome_RT_data.x,
            y: this.rome_RT_data.y,
            type: 'bar'
          };
          var data = [trace1];
          var layout = {
            // remove the layout of title

          };
          var config = {responsive: true, displayModeBar: false}
          Plotly.newPlot('rome_RT', data, layout, config);
      }
    }
  }
  </script>

  <style scoped>
  </style>