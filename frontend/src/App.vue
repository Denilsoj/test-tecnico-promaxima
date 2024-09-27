<template>
  <v-app>
    <v-container>
      <medicine-list></medicine-list> <!-- Uso do componente MedicineList -->
    </v-container>
  </v-app>
</template>

<script>
import MedicineList from './components/MedicineList.vue'; // Importando o componente

export default {
  components: {
    MedicineList, // Registrando o componente
  },
};
</script>