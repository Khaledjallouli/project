
<script>
import SidebarLink from "./SidebarLink.vue";

export default{
  name: "side-bar",
  components: {
    SidebarLink
  },
  props: {
    abv: {
      type: String,
      default: "CT"
    },
    title: {
      type: String,
      default: "Creative Tim"
    },
    backgroundColor: {
      type: String,
      default: "green"
    },
    sidebarLinks:{
      type: Array,
      default: () => []
    }
  },
  data(){
    return{
      activeLinkIndex: 0
    }
  },
  computed:{
    isRTL() {
      return this.$rtl.isRTL;
    }
  },
  methods:{
    findActiveLink(){
      this.links.forEach((link, index) => {
        if(link.isActive()){
          this.activeLinkIndex = index;
        }
      });
    }
  }
}
</script>
<style>
</style>
