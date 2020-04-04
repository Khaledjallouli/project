<template>
</template>
<script>
  export default {
    props:{
      backgroundColor: String
    },
    data(){
      return {
        isOpen: false,
        sidebarColors: [
          { color: 'primary', active: false, value: 'primary' },
          { color: 'info', active: false, value: 'blue' },
          { color: 'success', active: false, value: 'green' }
        ]
      }
    },
    methods:{
      toggleDropDown(){
        this.isOpen = !this.isOpen
      },
      closeDropDown(){
        this.isOpen = false
      },
      toggleList(list, itemToActivate) {
        list.forEach((listItem) => {
          listItem.active = false
        });
        itemToActivate.active = true
      },
      changeSidebarBackground(item){
        this.$emit('update:backgroundColor', item.value)
        this.toggleList(this.sidebarColors, item)
      }
    }
  }
</script>
<style>
</style>
