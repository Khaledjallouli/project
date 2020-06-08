<template>
  <div class="content">
    <div class="gamePrediction">Soccer Games Prediction</div>
    <div class="tableMatches">
      <div id="gridtitle">
        <div class="col">
          <div class="section">Home Team</div>
          <hr />
        </div>
        <div class="col">
          <div class="section">Away Team</div>
          <hr />
        </div>
        <div class="col">
          <div class="section">Date Match</div>
          <hr />
        </div>
        <div class="col">
          <div class="section">Final Result</div>
          <hr />
        </div>
      </div>

      <b-table
        v-for="(item,index) in  this.SoccerGamesList.SoccerGames"
        :key="index"
        :items="items"
        :fields="index"
      >
        <soccer-game bottom-nav v-bind="item"></soccer-game>
      </b-table>
    </div>

    <div></div>
  </div>
</template>
<script>
import axios from "axios";
import SoccerGame from "@/components/SoccerGames/SoccerGame";

export default {
  components: {
    SoccerGame
  },
  data: () => ({
    SoccerGamesList: null
  }),
  created() {
    console.log("route: ", this.$route);
    if (!this.SoccerGamesList) {
      this.getSGData();
    }
  },
  beforeMount() {
    this.getSGData();
  },
  methods: {
    getSGData: function getSGData() {
      axios.get(`http://127.0.0.1:5000/soccerGames`).then(response => {
        this.SoccerGamesList = response.data;
      });
    }
  }
};
</script>
<style>
.gameAttributesHome {
  list-style-type: none;
  margin: 0;
  padding: 10px;
  padding-top: 20px;
  overflow: hidden;
}
.gameAttributesHome li {
  float: left;
  margin-right: 140px;
  margin-left: 38px;
  text-align: center;
  font-weight: bold;
}

.gamePrediction {
  text-align: left;
  color: rgb(134, 134, 134);
  font-size: 20px;
  padding-bottom: 10px;
}

#gridtitle {
  margin-left: -15px;
  font-weight: bold;
}

.col {
  width: 25%;
  float: left;
}

.section {
  margin-left: 15px;
  height: 40px;
}
</style>
