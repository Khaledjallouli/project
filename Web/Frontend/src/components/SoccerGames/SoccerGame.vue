<template>
  <div class="soccer-game">
    <v-card ref="soccergame">
      <v-card-text v-bind:style="{backgroundColor: this.backgroundColor}">
        <div id="grid">
          <div class="col">
            <div class="section">{{homeTeam}}</div>
            <hr />
          </div>
          <div class="col">
            <div class="section">{{awayTeam}}</div>
            <hr />
          </div>
          <div class="col">
            <div class="section">{{dateMatch}}</div>
            <hr />
          </div>
          <div class="col">
            <div class="section">{{originalFinalResultText}}</div>
            <hr />
          </div>
          <div class="col">
            <div class="section">{{predictedFinalResultText}}</div>
            <hr />
          </div>
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    homeTeam: {
      type: String,
      default: ""
    },
    awayTeam: {
      type: String,
      default: ""
    },
    dateMatch: {
      type: String,
      default: ""
    },
    predictedResult: {
      type: String,
      default: ""
    },
    actualResult: {
      type: String,
      default: ""
    }
  },
  data: () => ({
    backgroundColor: "",
    predictedFinalResultText: "",
    originalFinalResultText: ""
  }),
  beforeMount() {
    if ("H" == this.predictedResult) {
      this.predictedFinalResultText = "Win Home Team";
    } else if ("A" == this.predictedResult) {
      this.predictedFinalResultText = "Win Away Team";
    } else if ("D" == this.predictedResult) {
      this.predictedFinalResultText = "Draw";
    }
    else {
      this.predictedFinalResultText = this.predictedResult;
    }

    if ("H" == this.actualResult) {
      this.originalFinalResultText = "Win Home Team";
    } else if ("A" == this.actualResult) {
      this.originalFinalResultText = "Win Away Team";
    } else if ("D" == this.actualResult) {
      this.originalFinalResultText = "Draw";
    }
    else {
      this.originalFinalResultText = this.actualResult;
    }

  }
};
</script>

<style lang="stylus" scoped>
.subheading {
  font-weight: 500;
  text-align: center;
}

.gameAttributes {
  list-style-type: none;
  margin: 0;
  padding: 10px;
  overflow: hidden;
}

.gameAttributes li {
  float: left;
  text-align: center;
  margin-right: 140px;
  margin-left: 45px;
}

tr {
  border-collapse: collapse;
  width: 100%;
}

#grid {
  margin-top: 30px;
  margin-left: -15px;
}

.col {
  width: 20%;
  float: left;
}

.section {
  margin-left: 15px;
  height: 50px;
  padding-top: 15px;
}
</style>