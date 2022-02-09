<template>
  <div class="home container">
    <div class="row">
    <ImportDeck class="col-xl"/>
    <Decklists class="col-xl"/>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Decklists from '@/components/Decklists.vue'
import ImportDeck from '@/components/ImportDeck.vue'

export default {
  name: 'Home',
  components: {
    Decklists,
    ImportDeck
  }
}
</script>
