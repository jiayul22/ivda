<template>
    <main>
        <div id='paris_RT' style="height:350px; width:90%; margin: auto; text-align: center;"></div>
    </main>
  </template>

  <script>
  import Plotly from 'plotly.js/dist/plotly';

  export default {
    data: () => ({
        paris_RT_data: {x: ['Entire home/apt', 'Private room', 'Hotel room', 'Shared room'], y: [51712, 8219, 1060, 373]},
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
            x: this.paris_RT_data.x,
            y: this.paris_RT_data.y,
            type: 'bar'
          };
          var data = [trace1];
          var layout = {
            // remove the layout of title

          };
          var config = {responsive: true, displayModeBar: false}
          Plotly.newPlot('paris_RT', data, layout, config);
      }
    }
  }
  </script>

  <style scoped>
  </style>