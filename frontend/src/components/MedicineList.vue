<template>
  <v-container>
    <v-data-table-virtual
      :headers="headers"
      :items="medicines"
      :items-per-page="itemsPerPage"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar style="height: 120px; padding: 30px; position: relative;" >
          <v-toolbar-title id="title">Medicamentos</v-toolbar-title>
          <div class="searchBarContainer">
            <SearchBar @search="handleSearch" class="searchBar"/>
          </div>
        </v-toolbar>
      </template>
    </v-data-table-virtual>

    <v-pagination
      v-model="currentPage"
      :length="totalPages"
      @input="fetchMedicines"
    ></v-pagination>
  </v-container>
</template>

<script>
import SearchBar from './SearchBar.vue'; 

export default {
  components: {
    SearchBar, 
  },
  data() {
    return {
      medicines: [],
      headers: [
        { title: 'ID', value: 'id', align: 'center' },
        { title: 'Substância', value: 'substance', align: 'center' },
        { title: 'CNPJ', value: 'cnpj', align: 'center' },
        { title: 'Laboratório', value: 'laboratory', align: 'center' },
      ],
      currentPage: 1,
      itemsPerPage: 25,
      totalPages: 0,
      filters: {
        substance: '',
        cnpj: '',
        laboratory: '',
      },
    };
  },
  
  methods: {
    async fetchMedicines() {
      const response = await fetch(`http://127.0.0.1:8000/api/?page=${this.currentPage}&substance=${this.filters.substance}&cnpj=${this.filters.cnpj}&laboratory=${this.filters.laboratory}`);
      const data = await response.json();
      
      this.medicines = data.results;
      this.totalPages = Math.ceil(data.count / this.itemsPerPage);
    },
    
    handleSearch(filters) {
      console.log('clicou')
      function resetFilters(filters) {
        if (filters.substance === null) {
            filters.substance = '';
        }
        
        if (filters.cnpj === null) {
            filters.cnpj = '';
        }
        
        if (filters.laboratory === null) {
            filters.laboratory = '';
        }
        
        
        if (filters.substance === null && filters.cnpj === null && filters.laboratory === null) {
            filters.substance = '';
            filters.cnpj = '';
            filters.laboratory = '';
        }
      }
      resetFilters(filters)
      this.filters = filters; 
      this.currentPage = 1; 
      this.fetchMedicines(); 
    },
    
  },
  
  watch: {
    currentPage(newPage) {
      this.fetchMedicines(); // Recarregar os dados quando a página mudar
    },
  },

  mounted() {
    this.fetchMedicines(); // Carrega os medicamentos ao montar o componente
  },
};
</script>

<style scoped>
#title {
   text-align: center;
   font-size: 25px;
   font-weight: bold;
   
}
.searchBarContainer{
  background-color: transparent;

}
@media (max-width: 588px) {
  /* Estilos para telas com largura máxima de 588px */
  
  #title {
    display: none; /* Diminui o tamanho da fonte do título */
  }
}
</style>