<template>
  <div class="soccer-game">
    <v-card ref="soccergame">
      <v-card-text v-bind:style="{ backgroundColor: this.backgroundColor}">
        <div class="layout ma-0 align-center">
          <div class="flex" :class="computeTextAlgin">
            <div class="subheading" v-bind:style="{ backgroundColor: this.backgroundColor}">
              <ul class="gameAttributes">
                <li>{{homeTeam}}</li>
                <li>{{awayTeam}}</li>
                <li>{{dateMatch}}</li>
                <li>{{finalResultText}}</li>
              </ul>
              <hr />
            </div>
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
    finalResult: {
      type: String,
      default: ""
    }
  },
  data: () => ({
    backgroundColor: "",
    finalResultText: ""
  }),
  beforeMount() {
    if (0 == this.finalResult) {
      //this.backgroundColor = "#aba4a3";
      this.finalResultText = "Draw";
    } else if (1 == this.finalResult) {
      //this.backgroundColor = "#23822a";
      this.finalResultText = "Win Home Team";
    } else if (2 == this.finalResult) {
      //this.backgroundColor = "#b82c21";
      this.finalResultText = "Win Away Team";
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
</style>