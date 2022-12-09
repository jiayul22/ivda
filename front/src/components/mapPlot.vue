<template>
  <v-card height="520">
    <v-btn @click="recenterZurich()">
      Zurich
    </v-btn>
    <v-btn  @click="recenterBerlin()">
      Berlin
    </v-btn>
    <v-btn  @click="recenterCopenhagen()">
      Copenhagen
    </v-btn>
    <v-btn  @click="recenterOslo()">
      Oslo
    </v-btn>
    <v-btn  @click="recenterParis()">
      Paris
    </v-btn>
    <v-btn  @click="recenterRome()">
      Rome
    </v-btn>
    <v-btn  @click="recenterSF()">
      San Francisco
    </v-btn>
    <v-btn  @click="recenterStockholm()">
      Stockholm
    </v-btn>
    <div>{{marker[0]}}</div>
  <div style="height: 400px; width: 100%">
    <l-map
        ref="map"
        v-if="showMap"
        :zoom="zoom"
        :center="center"
        :options="mapOptions"
        style="height: 100%"
        @update:center="centerUpdate"
        @update:zoom="zoomUpdate"

    >
      <l-tile-layer
          :url="url"
          :attribution="attribution"
      />
      <l-marker v-for="coordinate in marker" :lat-lng="coordinate" :key="coordinate.price">
        <l-popup :content="coordinate.price"/>
        <l-icon :icon-size="dynamicSize"/>

      </l-marker>
    </l-map>
  </div>

  </v-card>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup} from "vue2-leaflet";

export default {
  /*mounted() {

    this.property = 'Example property update.'

    console.log('propertyComputed will update, as this.property is now reactive.')

  },*/
  name: "ScatterPlot",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup
  },
  data() {
    return {
      zoom: 13,
      center: latLng(47.36667, 8.5500),
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
          '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      currentZoom: 11.5,
      currentCenter: latLng(47.36667, 8.550),
      markerLatLng: [],
      showParagraph: false,
      marker: [],
      mapOptions: {
        zoomSnap: 0.5
      },
      showMap: true,
      iconSize: 32
    };
  },
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    recenterZurich() {
      this.$refs.map.mapObject.setView([47.36667, 8.550],11);
      this.getdata('zurich')
    },
    recenterBerlin() {
      this.$refs.map.mapObject.setView([52.52, 13.404954],11);
      this.getdata('berlin')
    },
    recenterCopenhagen() {
      this.$refs.map.mapObject.setView([55.676098, 12.568337],11);
      this.getdata('copenhagen')
    },
    recenterOslo() {
      this.$refs.map.mapObject.setView([59.911491, 10.757933],11);
      this.getdata('oslo')
    },
    recenterParis() {
      this.$refs.map.mapObject.setView([48.864716, 2.349014],12);
      this.getdata('paris')
    },
    recenterRome() {
      this.$refs.map.mapObject.setView([41.902782, 12.496366],12);
      this.getdata('rome')
    },
    recenterSF() {
      this.$refs.map.mapObject.setView([37.773972, -122.431297],12);
      this.getdata('san francisco')
    },
    recenterStockholm() {
      this.$refs.map.mapObject.setView([59.334591, 18.063240],12);
      this.getdata('stockholm')
    },
    async getdata(city)
    {
      var reqUrl = `http://127.0.0.1:5000/map?city=${city}`
      console.log("ReqURL " + reqUrl)
      // await response
      const response = await fetch(reqUrl)
      const responseData = await response.json();
      this.marker = responseData['out']

    }
  },
    mounted() {

    },
  computed: {
    dynamicSize () {
      return [this.iconSize, this.iconSize * 1.15]
    }
  }


};
</script>
