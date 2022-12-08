<template>
    <main>
        <div id='stockholm_RT' style="height:350px; width:90%; margin: auto; text-align: center;"></div>
    </main>
  </template>

  <script>
  import Plotly from 'plotly.js/dist/plotly';

  export default {
    data: () => ({
        stockholm_RT_data: {x: ['Entire home/apt', 'Private room', 'Hotel room', 'Shared room'], y: [3065, 832, 43, 50]},
    }),

    mounted() {
      this.fetchData()
    },

    methods: {
      fetchData() {
          // draw the lineplot after the data is transtockholmormed
          this.drawLinePlot()
        },
      drawLinePlot() {
          var trace1 = {
            x: this.stockholm_RT_data.x,
            y: this.stockholm_RT_data.y,
            type: 'bar'
          };
          var data = [trace1];
          var layout = {
            // remove the layout of title

          };
          var config = {responsive: true, displayModeBar: false}
          Plotly.newPlot('stockholm_RT', data, layout, config);
      }
    }
  }
  </script>

  <style scoped>
  </style>