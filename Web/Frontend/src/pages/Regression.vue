<template>
  <div class="content">
    <div class="row">
      <div class="col-md-12">
        <card>
          <div class="row">
            <div class="col-md-6 ml-auto mr-auto text-center">
              <h4 class="card-title">
                <b>Retrain and Fetch New Matches</b>
              </h4>
            </div>
          </div>
          <div class="row">
            <div class="col-lg-8 ml-auto mr-auto">
              <div class="row">
                <div class="col-md-4">
                  <base-button
                    type="warning"
                    block
                    @click="notifyVueRetrain('top', 'left')"
                  >Retrain</base-button>
                </div>
                <div class="col-md-4">
                  <!--<base-button type="primary" block @click="notifyVue('top', 'center')">Top Center</base-button> -->
                </div>
                <div class="col-md-4">
                  <base-button
                    type="warning"
                    block
                    @click="notifyVueFetch('top', 'right')"
                  >Fetch New Matches</base-button>
                </div>
              </div>
            </div>
          </div>
        </card>
      </div>
    </div>
    <div class="gamePrediction">Soccer Games Prediction - Goals</div>
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
          <div class="section">Actual Goals</div>
          <hr />
        </div>
        <div class="col">
          <div class="section">Predicted Goals</div>
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
  </div>
</template>
<script>
import axios from "axios";
import SoccerGame from "@/components/SoccerGames/SoccerGame";
import { Card } from "@/components/index";

import BaseAlert from "@/components/BaseAlert";
import BaseButton from "@/components/BaseButton";
import NotificationTemplate from "./Notifications/NotificationTemplate";
import NotificationTemplateFetch from "./Notifications/NotificationTemplateFetch";

export default {
  components: {
    BaseAlert,
    BaseButton,
    Card,
    SoccerGame
  },
  data: () => ({
    type: ["", "info", "success", "warning", "danger"],

    notifications: {
      topCenter: false
    },
    SoccerGamesList: null,
    fetch: "",
    retrain: ""
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
      axios
        .get(`http://127.0.0.1:5000/soccerMatchesRegression`)
        .then(response => {
          this.SoccerGamesList = response.data;
        })
        .catch(error => {
          this.SoccerGamesList = "ERROR: API-calls doesn’t work";
          this.$alert("ERROR: API calls don't work.");
        });
    },
    getFetchNewMatches: function getFetchNewMatches() {
      axios.get(`http://127.0.0.1:5000/fetchNewMatches`).then(response => {
        this.fetch = response.data;
      });
    },

    getRetrainRegression: function getRetrainRegression() {
      axios.get(`http://127.0.0.1:5000/retrainRegression`).then(response => {
        this.retrain = response.data;
      });
    },
    notifyVueRetrain(verticalAlign, horizontalAlign) {
      const color = Math.floor(Math.random() * 4 + 1);
      this.getRetrainRegression();
      this.$notify({
        component: NotificationTemplate,
        icon: "tim-icons icon-bell-55",
        horizontalAlign: horizontalAlign,
        verticalAlign: verticalAlign,
        type: this.type[color],
        timeout: 0
      });
    },
    notifyVueFetch(verticalAlign, horizontalAlign) {
      const color = Math.floor(Math.random() * 4 + 1);
      this.getFetchNewMatches();
      this.$notify({
        component: NotificationTemplateFetch,
        icon: "tim-icons icon-bell-55",
        horizontalAlign: horizontalAlign,
        verticalAlign: verticalAlign,
        type: this.type[color],
        timeout: 0
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
  width: 20%;
  float: left;
}

.section {
  margin-left: 15px;
  height: 40px;
}
</style>
