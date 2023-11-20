<script>
  export default {
    data() {
      return {
        ticketQuantity: {
          padrao: 0,
          vip: 0,
          premium: 0,
        },
        totalPrice: 0,
        selectedPrices: {
          padrao: 50,
          vip: 100,
          premium: 150,
        },
      };
    },
    methods: {
      handleSelectTicket(price, type) {
        this.$set(this.ticketQuantity, type, this.ticketQuantity[type] + 1);
        this.calculateTotalPrice();
      },
      decrementQuantity(type) {
        if (this.ticketQuantity[type] > 0) {
          this.$set(this.ticketQuantity, type, this.ticketQuantity[type] - 1);
          this.calculateTotalPrice();
        }
      },
      calculateTotalPrice() {
        this.totalPrice = Object.keys(this.ticketQuantity).reduce(
          (acc, ticketType) =>
            acc + this.selectedPrices[ticketType] * this.ticketQuantity[ticketType],
          0
        );
      },
      handleConfirmarCompra() {
        if (this.totalPrice > 0) {
          // Navegue para a página de pagamento ou execute a lógica desejada
          console.log('Navegar para a página de pagamento');
        }
      },
    },
  };
</script>
<template>
    <div class="container">
      <h1 class="title">Compra de Ingresso</h1>
      <div class="ticket-container">
        <p class="ticket-title">Escolha o tipo de ingresso:</p>
        <div v-for="(price, type) in selectedPrices" :key="type" class="ticket-option-container">
          <div class="ticket-option" @click="handleSelectTicket(price, type)">
            <p class="option-text">Ingresso {{ type }}</p>
            <p class="option-price">R$ {{ price }}</p>
          </div>
          <div class="quantity-container">
            <button class="quantity-button" @click="decrementQuantity(type)">-</button>
            <p class="quantity-text">{{ ticketQuantity[type] }}</p>
            <button class="quantity-button" @click="handleSelectTicket(price, type)">+</button>
          </div>
        </div>
        <p class="total-geral">Total Geral: R$ {{ totalPrice }}</p>
        <button
          class="confirm-purchase-button"
          :style="{ backgroundColor: totalPrice > 0 ? '#28a745' : '#ccc' }"
          @click="handleConfirmarCompra"
          :disabled="totalPrice <= 0"
        >
          Confirmar Compra
        </button>
      </div>
    </div>
  </template>
  
  
  
  <style scoped>
  .container {
    flex: 1;
    background-color: #f9f9f9;
    align-items: center;
    padding-top: 40px;
  }
  
  .title {
    font-size: 30px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
  }
  
  .ticket-container {
    border-width: 2px;
    border-color: #ccc;
    border-radius: 10px;
    padding: 20px;
    width: 80%;
  }
  
  .ticket-title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 15px;
    color: #333;
  }
  
  .ticket-option-container {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
  }
  
  .ticket-option {
    flex: 1;
    padding: 10px;
    background-color: #f2f2f2;
    border-radius: 10px;
    margin-right: 10px;
  }
  
  .option-text {
    font-size: 18px;
    color: #333;
  }
  
  .option-price {
    font-size: 18px;
    font-weight: bold;
    color: #800000;
  }
  
  .quantity-container {
    flex-direction: row;
    align-items: center;
  }
  
  .quantity-button {
    background-color: #007bff;
    border-radius: 15px;
    padding: 10px;
  }
  
  .quantity-button-text {
    font-size: 18px;
    font-weight: bold;
    color: #fff;
  }
  
  .quantity-text {
    font-size: 18px;
    font-weight: bold;
  }
  
  .total-geral {
    padding-bottom: 20px;
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
    color: #333;
  }
  
  .confirm-purchase-button {
    background-color: #28a745;
    border-radius: 10px;
    padding: 10px;
    align-items: center;
    margin-top: 10px;
  }
  
  .confirm-purchase-button-text {
    font-size: 18px;
    font-weight: bold;
    color: #fff;
  }
  </style>
  