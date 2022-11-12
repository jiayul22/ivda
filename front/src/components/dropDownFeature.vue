<template>
  <v-card height="420">
  
    <v-list-item
      v-for="(item, i) in selectCategory"
      :key="i"
    >
      <v-combobox
        :items="item.value"
        :label=item.name
        filled
        height=5
        @change="onChange($event,item.name)"
      ></v-combobox>
    </v-list-item>


    <v-btn
      elevation="2"
       @click="sendSelectionToBackend"
    >
      Submit
    </v-btn>

  </v-card>
</template>

<script>
export default {

  name: "dropDownFeature",

  data: () => ({
    inputFeature:{
      'City':'', 
      'Region':'',
      'Room_Type':'',
      'Available_Night':'',
    },
    selectCategory: [
      {name: 'City', value: ['Berlin', 'Cophenhagen', 'Oslo', 'Paris', 'Rome', 'San-francisco', 'Stockholm', 'Zurich']},
      {name: 'Region' , value: ['R1','R2','R3']},
      {name: 'Room_Type', value: ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room']},
      {name: 'Minimum nights',value:[]},
      {name: 'Available_365',value:[]},
    ]
  }),

  methods: {
      async sendSelectionToBackend () {
        var paras = ''
        for (const [key, value] of Object.entries(this.inputFeature)) {
          console.log('输出',key, value);
          paras = paras+key+'='+value+'&'
        }
        console.log("参数" + paras)
        var reqUrl = 'http://127.0.0.1:5000/PredictPrice?'+paras
        console.log("ReqURL " + reqUrl)

        // await response and data
        const response = await fetch(reqUrl)
        const responseData = await response.json();
        console.log("responseData " + responseData )
      },

      onChange(value,name){
        //
        console.log('输入：',name, value);
        this.inputFeature[name] = value;
      }
  },
  
  
}
</script>

<style scoped>
  .select.v-text-field.v-text-field--enclosed:not(.v-text-field--rounded)>.v-input__control>.v-input__slot {
  padding-right: 4px
}
</style>
