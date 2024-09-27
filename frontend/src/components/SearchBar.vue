<template>
    <div class="container">
        <v-form>
            <v-row>
            <v-col>
                <v-text-field
                v-model="substance"
                label="Substância"
                outlined
                clearable
                width="120"
                class="textField"
                />
            </v-col>
            <v-col  class="cnpjContainer">
                <v-text-field
                v-model="cnpj"
                label="CNPJ"
                outlined
                clearable
                width="80"
                />
            </v-col>
            <v-col class="laboratoryContainer">
                <v-text-field
                v-model="laboratory"
                label="Laboratório"
                outlined
                clearable
                width="120"
                />
            </v-col>
            </v-row>
        </v-form>
        <v-btn
          @click="searchMedicines"
          color="primary"
          class="ml-2"
        >
          <v-icon left>mdi-magnify</v-icon> 
        </v-btn>
       
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        substance: '',
        cnpj: '',
        laboratory: '',
      };
    },
    methods: {
      searchMedicines() {
        this.$emit('search', {
          substance: this.substance,
          cnpj: this.cnpj,
          laboratory: this.laboratory,
        });
      },
    },
  };
  </script>
  
  <style scoped>
  .container{
    background-color: transparent;
    display: flex;
    align-items: center;

  }

  @media (max-width: 588px) {
  
  
  .laboratoryContainer {
    display: none; 
  }
}
@media (max-width: 422px) {
 
  
  .cnpjContainer {
    display: none; 
  }
}
  
 
  </style>
  