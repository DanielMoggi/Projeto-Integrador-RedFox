<script>
import LoginUser from './components/LoginUser.vue';
import CadastroUser from './components/CadastroUser.vue';
import HistoricoScreen from './components/HistoricoScreen.vue';
import IngressoScreen from './components/IngressoScreen.vue';
import PagamentoScreen from './components/PagamentoScreen.vue';

export default {
  components: {
    CadastroUser,
    LoginUser,
    PagamentoScreen,
    HistoricoScreen,
    IngressoScreen
  }
};

</script>

<template>
   <div id="app">
    <LoginUser />
  </div>
</template>

<style scoped>
.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    
  }
}
</style>
