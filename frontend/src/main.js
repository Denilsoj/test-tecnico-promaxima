import { createApp } from 'vue';
import App from './App.vue';

// Importando o Vuetify e os estilos
import { createVuetify } from 'vuetify';
import 'vuetify/styles';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

// Importando ícones e temas (opcional)
import '@mdi/font/css/materialdesignicons.css';

// Criação da instância do Vuetify
const vuetify = createVuetify({
    components,
    directives,
  });
  
const app = createApp(App);

// Registrando o Vuetify na aplicação
app.use(vuetify);

app.mount('#app');
