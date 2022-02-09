<template>
  <div class="decklists">
    <div v-for="(value, key, index) in decklists" :key="index">
        {{key}}
    </div>
  </div>
</template>
<script>
import backend from '../apis/backend'
export default {
  name: "Decklists",
  props: {},
  data() {
    return {
      decklists: {},
    };
  },
  methods: {
    loadDeckLists()
    {
      backend.getDeckLists().then(response => {
        console.log(response.data)
        console.log(response.data.deckLists)
        this.decklists = response.data.deckLists
        })
    }
  },
  mounted() {
    this.loadDeckLists()
  },
};
</script>
<style>
</style>
