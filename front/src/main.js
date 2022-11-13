import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'

import HistogramSlider from "vue-histogram-slider";
import "vue-histogram-slider/dist/histogram-slider.css";

Vue.component(HistogramSlider.name, HistogramSlider);

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
