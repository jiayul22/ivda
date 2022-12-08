<template>
    <main>
        <div id='zurich_RT' style="height:350px; width:90%; margin: auto; text-align: center;"></div>
    </main>
  </template>

  <script>
  import Plotly from 'plotly.js/dist/plotly';

  export default {
    data: () => ({
        zurich_RT_data: {x: ['Entire home/apt', 'Private room', 'Hotel room', 'Shared room'], y: [1532, 687, 9, 18]},
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
            x: this.zurich_RT_data.x,
            y: this.zurich_RT_data.y,
            type: 'bar'
          };
          var data = [trace1];
          var layout = {
            // remove the layout of title

          };
          var config = {responsive: true, displayModeBar: false}
          Plotly.newPlot('zurich_RT', data, layout, config);
      }
    }
  }
  </script>

  <style scoped>
  </style>