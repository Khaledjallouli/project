import DashboardLayout from "@/pages/Layout/DashboardLayout.vue";

import Dashboard from "@/pages/Home.vue";


const routes = [{
  path: "/",
  component: DashboardLayout,
  redirect: "home",
  children:[
    {
      path: "home",
      name: "home",
      component: Dashboard
    }
  ]

}];

export default routes;
