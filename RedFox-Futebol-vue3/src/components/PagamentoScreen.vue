<script>
  export default {
    data() {
      return {
        nome: '',
        numeroCartao: '',
        dataExpiracao: '',
        codigoSeguranca: '',
      };
    },
    methods: {
      handleRealizarPagamento() {
        // Lógica para confirmar o pagamento
        alert('Pagamento Efetuado', 'Pagamento efetuado com sucesso!');
      },
    },
  };
</script>
<template>
    <div class="container">
      <h1 class="title">Confirmação de Pagamento</h1>
      <div class="input-container">
        <label class="label">Nome no Cartão:</label>
        <input v-model="nome" class="input" placeholder="Nome no Cartão" />
      </div>
      <div class="input-container">
        <label class="label">Número do Cartão:</label>
        <input v-model="numeroCartao" class="input" placeholder="Número do Cartão" />
      </div>
      <div class="input-container">
        <label class="label">Data de Expiração:</label>
        <input v-model="dataExpiracao" class="input" placeholder="MM/AA" />
      </div>
      <div class="input-container">
        <label class="label">Código de Segurança:</label>
        <input v-model="codigoSeguranca" class="input" placeholder="Código de Segurança" />
      </div>
      <button @click="handleRealizarPagamento" class="button">Confirmar Pagamento</button>
    </div>
  </template>
  
  <style scoped>
  .container {
    flex: 1;
    padding: 16px;
    background-color: #f5f5f5;
    align-items: center;
    justify-content: center;
  }
  
  .title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 16px;
  }
  
  .input-container {
    margin-bottom: 16px;
    width: 100%;
  }
  
  .label {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 8px;
  }
  
  .input {
    height: 40px;
    border: 1px solid gray;
    padding: 0 12px;
    border-radius: 8px;
  }
  
  .button {
    background-color: #007BFF;
    padding: 14px;
    border-radius: 8px;
    align-items: center;
    width: 100%;
    color: #fff;
    font-size: 18px;
    font-weight: bold;
  }
  </style>
  