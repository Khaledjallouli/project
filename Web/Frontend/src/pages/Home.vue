<template>
  <div class="content">
    <div class="row">
      <div class="col-12">
        <card>
          <template slot="header">
            <h4 class="card-title">Soccer Games Prediction</h4>
          </template>
          <div>
            <base-table :data="table1.data"
                        :columns="table1.columns"
                        thead-classes="text-primary">
            </base-table>
          </div>
        </card>
      </div>

      <div class="col-12">
        <card class="card-plain">
          <template slot="header">
                <h4 class="card-title"> Soccer Games Prediction</h4>
              </template>
          <div class="table-full-width">
            <base-table :title="table2.title" :sub-title="table2.subTitle" :data="table2.data"
                        :columns="table2.columns">
            </base-table>
          </div>
        </card>
      </div>

    </div>
  </div>
</template>
<script>

import {
  Card
} from "@/components/index";

import BaseTable from "@/components/BaseTable";

const tableColumns = ["HomeTeam", "AwayTeam","FinalResult"];
const tableData = [
  {
    id: 1,
    hometeam: "FC Bayern Munich",
    awayteam: "Borussia Dortmund",
    finalresult: "Win Home Team"
  },
  {
    id: 2,
    hometeam: "FC Bayern Munich",
    awayteam: "Borussia Dortmund",
    finalresult: "Win Home Team"
  },
  {
    id: 3,
    hometeam: "FC Bayern Munich",
    awayteam: "Borussia Dortmund",
    finalresult: "Win Home Team"
  },
  {
    id: 4,
    hometeam: "FC Bayern Munich",
    awayteam: "Borussia Dortmund",
    finalresult: "Win Home Team"
  },
  {
    id: 5,
    hometeam: "FC Bayern Munich",
    awayteam: "Borussia Dortmund",
    finalresult: "Win Home Team"
  },
  {
    id: 6,
    hometeam: "FC Bayern Munich",
    awayteam: "Borussia Dortmund",
    finalresult: "Win Home Team"
  },
  {
    id: 7,
    hometeam: "FC Bayern Munich",
    awayteam: "Borussia Dortmund",
    finalresult: "Win Home Team"
  }
];


export default{
  components:{
    Card,
    BaseTable
  },
  data() {
    return {
      table1: {
        title: "Simple Table",
        columns: [...tableColumns],
        data: [...tableData]
      },
      table2: {
        title: "Table on Plain Background",
        columns: [...tableColumns],
        data: [...tableData]
      }
    };
  }
}
</script>
<style>
</style>
