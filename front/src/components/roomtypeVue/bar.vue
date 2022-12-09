<template>
    <main>
        <div id='bar' style="height:350px; width:90%; margin: auto; text-align: center;"></div>
    </main>
  </template>

  <script>
  import Plotly from 'plotly.js/dist/plotly';

  export default {
    data: () => ({
        outData: {x: ['Entire home/apt', 'Private room', 'Hotel room', 'Shared room'], y: [0, 0, 0, 0]},
    }),

    mounted() {
      this.drawLinePlot()
    },

    methods: {
      fetchData() {
          // draw the lineplot after the data is transformed
          this.drawLinePlot()
        },
      drawLinePlot() {
        const data = [this.outData];
        const layout = {
          // remove the layout of title
        };
        const config = {responsive: true, displayModeBar: false}
        Plotly.newPlot('bar', data, layout, config);
      }
      }
    }
  }
  </script>

  <style scoped>
  </style>