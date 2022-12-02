<template>
  <v-container
    fluid
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col 
        cols="12" md="3" 
        class="mt-0 pa-1"
      >
        <v-card height="500">

          <v-list-item
            v-for="(item, i) in selectCategory"
            :key="i"
          >
            <v-combobox
              :items="item.value"
              :label=item.name
              filled
              height=5
              @change="recordInput($event,item.name)"
            ></v-combobox>
          </v-list-item>

          <v-col class="text-right">
            <v-btn
              elevation="2"
              @click="sendSelectionToBackend"
            >
              Submit
            </v-btn>
          </v-col>
            
        </v-card>
      </v-col>

      <v-col cols="12" md="2" class="mt-0 pa-1">
        <v-card height="500">
          <PredictionPrice 
            :price="price"
            :neighborhood_avg="neighborhood_avg"
            :name_score="name_score"
          />
        </v-card>
      </v-col>

      <v-col cols="12" md="5" class="mt-0 pa-1">
        <v-card height="500">
          <PredictionFeatureWeight
            :key="barPlotId"
            :weights="weights"
          />
        </v-card>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
import PredictionFeatureWeight from './PredictionFeatureWeight';
import PredictionPrice from './PredictionPrice';

export default {
  
  name: "dropDownFeature",
  components: {PredictionFeatureWeight, PredictionPrice},

  data: () => ({
    barPlotId: 0,

    price:'',
    neighborhood_avg:'',
    weights:'',
    name_score:'',
    
    inputFeature:{
      'city':'', 
      'neighbourhood':'',
      'room_type':'',
      'minimum_nights':'',
      'name':''
    },
    selectCategory: [
      // TODO should read database to get full data
      {name: 'city', value: ['zurich','berlin']},
      {name: 'neighbourhood' , value: ['Sihlfeld', 'Alt-Wiedikon', 'Enge', 'Höngg', 'Wollishofen',
                                'Escher Wyss', 'Wipkingen', 'Gewerbeschule', 'Rathaus']},
      {name: 'room_type', value: ['Entire home/apt', 'Private room', 'Hotel room', 'Shared room']},
      {name: 'minimum_nights',value:''},
      {name: 'name', value:''},
    ]
  }),

  mounted() {
  },

  methods: {
      async sendSelectionToBackend () {
        this.barPlotId += 1

        // construct request
        var paras = ''
        for (const [key, value] of Object.entries(this.inputFeature)) {
          paras = paras+key+'='+value+'&'
        }
        var reqUrl = 'http://127.0.0.1:5000/PredictPrice?'+paras
        console.log("ReqURL " + reqUrl)

        // await response
        const response = await fetch(reqUrl)
        const responseData = await response.json();

        this.price = parseFloat(responseData.price) 
        this.neighborhood_avg = parseFloat(responseData.neighborhood_avg)
        this.weights = responseData.weights
        this.name_score = responseData.name_score

      },

      recordInput(value,name){
        // record input
        this.inputFeature[name] = value;
        this.barPlotId += 1
      },

      changeIndex(){
        this.barPlotId += 1
      }
  },
  
  
}
</script>

<style scoped>
  .select.v-text-field.v-text-field--enclosed:not(.v-text-field--rounded)>.v-input__control>.v-input__slot {
  padding-right: 4px
}
</style>
