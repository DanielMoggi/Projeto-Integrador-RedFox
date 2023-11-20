<template>
    <div>
      <div class="menu">
        <span class="menu-item">Home</span>
        <div class="search-bar">
          <img src="@/assets/pngwing.com.png" alt="lupa" class="lupa-icon" />
          <input v-model="searchInput" placeholder="Search" class="search-input" />
        </div>
        <div class="handle-historico">
          <button class="compra-button" @click="handleHistorico">
            <img :src="require('@/assets/pngfind.com-bite-mark-png-631239.png')" alt="profile" class="rounded-image" />
          </button>
        </div>
      </div>
  
      <div class="content">
        <h1 class="content-text">Jogos da semana</h1>
  
        <div class="image-row">
          <div v-for="(game, index) in games" :key="index" class="column">
            <img :src="game.team1" alt="team1" class="image" />
            <span class="vs-text">VS</span>
            <img :src="game.team2" alt="team2" class="image" />
            <button class="compra-button" @click="handleComprarIngresso">
              Comprar ingresso
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchInput: '',
        games: [
          { team1: require('./img/Botafogo.png'), team2: require('./img/Flamengo.png') },
          { team1: require('./img/América.png'), team2: require('./img/Bahia.png') },
          { team1: require('./img/Athletico Paranaense.png'), team2: require('./img/.png') },
          { team1: require('./img/Corinthians.png'), team2: require('./img/Cruzeiro.png') },
          { team1: require('./img/Cuiabá.png'), team2: require('./img/Palmeiras.png') },
          { team1: require('./img/Coritiba.png'), team2: require('./img/Fluminense.png') },
          { team1: require('./img/Fortaleza.png'), team2: require('./img/Goiás Esporte Clube-GO.png') },
          { team1: require('./img/São Paulo.png'), team2: require('./img/Internacional.png') },
        ],
      };
    },
    methods: {
      handleComprarIngresso() {
        this.$router.push({ name: 'Ingresso' });
      },
      handleHistorico() {
        this.$router.push({ name: 'Historico' });
      },
    },
  };
  </script>
  
  <style scoped>
  .menu {
    display: flex;
    align-items: center;
    background-color: gray;
    padding: 20px;
  }
  
  .menu-item {
    padding: 20px;
    color: #fff;
    font-size: 18px;
    margin-right: 10px;
  }
  
  .search-bar {
    display: flex;
    background-color: #fff;
    border-bottom: 1px solid #ccc;
    border-radius: 5px;
    flex: 1;
    align-items: center;
  }
  
  .lupa-icon {
    width: 20px;
    height: 20px;
    color: #000;
  }
  
  .search-input {
    border: none;
    padding: 5px;
    flex: 1;
  }
  
  .content {
    display: flex;
    flex-grow: 1;
    justify-content: center;
    padding: 20px;
    align-items: center;
    padding-bottom: 30px;
  }
  
  .content-text {
    font-size: 24px;
    margin-bottom: 20px;
    text-align: center;
    color: #000;
  }
  
  .image-row {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    padding: 10px;
  }
  
  .column {
    align-items: center;
    padding: 10px;
    width: 48%;
    margin-bottom: 20px;
    background-color: #fff;
  }
  
  .image {
    width: 100px;
    height: 100px;
    margin-bottom: 10px;
  }
  
  .vs-text {
    font-size: 18px;
    color: #000;
  }
  
  .compra-button {
    background-color: #800000;
    border-radius: 5px;
    padding: 10px 20px;
    margin-top: 10px;
    color: #fff;
    cursor: pointer;
  }
  </style>