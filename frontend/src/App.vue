<template>
  <v-app>
    <v-container>
      <medicine-list></medicine-list> 
    </v-container>
  </v-app>
</template>

<script>
import MedicineList from './components/MedicineList.vue'; 
export default {
  components: {
    MedicineList, 
  },
};
</script>