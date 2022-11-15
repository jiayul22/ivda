<template>
  <v-app id="inspire">

    <v-navigation-drawer
      v-model="drawer"
      app
      class="pt-4"
      color="grey lighten-3"
      mini-variant
    >
      <v-avatar
        v-for="n in 6"
        :key="n"
        :color="`grey ${n === 1 ? 'darken' : 'lighten'}-1`"
        :size="n === 1 ? 36 : 20"
        class="d-block text-center mx-auto mb-9"
      ></v-avatar>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="#43a047"
      dark
      src="https://picsum.photos/1920/1080?random"
      fade-img-on-scroll
      scroll-target="#scrolling-techniques-5"
      scroll-threshold="15"
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(55,236,186,.7), rgba(25,32,72,.7)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Dashboard For Hosts</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>

    <v-sheet
      id="scrolling-techniques-5"
      class="overflow-y-auto"
      max-height="600"
    >
      <v-container style="height: 0px;"></v-container>
    </v-sheet>

    <v-main>
      <v-container
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >

          <v-col cols="12" md="5" class="mt-0 pa-1">
            <mapPlot/>
          </v-col>

          <v-col cols="12" md="5" class="mt-0 pa-1">
            <histogram/>
          </v-col>

        </v-row>
      </v-container>

      <v-container
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
            <PredictionFeatureSelection/>

        </v-row>
      </v-container>

    </v-main>

  </v-app>
</template>

<script>
  import mapPlot from './components/mapPlot';
  import histogram from './components/histogram';
  import PredictionFeatureSelection from './components/PredictionFeatureSelection';

  export default {
    components: {
      mapPlot,
      histogram,
      PredictionFeatureSelection,
    },
    data: () => ({
      drawer: null,
      items: [
          { title: 'Dashboard', icon: 'format-list-chekcs', to:'/'},
          { title: 'Photos', icon: 'mdi-image' },
          { title: 'About_xx', icon: 'mdi-help-box', to:'/about' },
      ],
    }),
  }
</script>