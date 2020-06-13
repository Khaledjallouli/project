import DashboardLayout from "@/pages/Layout/DashboardLayout.vue";

import Dashboard from "@/pages/Home.vue";
import Icons from "@/pages/Regression.vue";


const routes = [{
  path: "/",
  component: DashboardLayout,
  redirect: "home",
  children:[
    {
      path: "home",
      name: "results",
      component: Dashboard
    },
    {
      path: "goals",
      name: "goals",
      component: Icons
    }
  ]

}];

export default routes;
