<template>
  <div>
    <v-combobox
        v-model="selectedCity"
        :items=city
        label="City"
        filled
        height=5
    ></v-combobox>
    <div>{{selectedCity}}</div>


  <l-map style="height: 500px" :zoom="zoom" :center="center">
  <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
  <l-marker :lat-lng="markerLatLng" ></l-marker>
  </l-map>
  </div>
</template>

<script>
import { marker } from 'leaflet';
import {LMap, LTileLayer, LMarker} from 'vue2-leaflet';

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 3,
      center: [47.313220, -1.319482],
      markerLatLng: []
    }
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetch_data() {
      for (var i=0; i<5; i++){
        var lat = Math.floor(Math.random() *88) + 1;
        lat *= Math.floor(Math.random() * 2) == 1 ? 1 : -1;

        var lng = Math.floor(Math.random() *88) + 1;
        lng *= Math.floor(Math.random() * 2) == 1 ? 1 : -1;
        
        this.markerLatLng.push([lat, lng])
        console.log(this.markerLatLng)
      }    
    },  

  created() {
      var coordinates = [[47.313220, -100.319482], [156.0, 48.0]]
      for (var i = 0; i < 2; i++) {
        var a = coordinates[i]
        this.markerLatLng.push(a)
      }
      console.log(this.markerLatLng)
    }
  }
};
</script>
