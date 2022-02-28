<template>
  <div class="decklists">
    <div>
      <h2>Saved decks</h2>
      <div class="form-group m-3">
        <label>Format</label>
        <select class="form-select" v-model="filter">
          <option value="all">All</option>
          <option v-for="(i, index) in formats" :key="index">{{ i }}</option>
        </select>
      </div>
      <div class="table-wrapper m-3">
        <table class="table table-sm">
          <thead>
            <tr>
              <th scope="col">Format</th>
              <th scope="col">Deck name</th>
              <th scope="col" class="col-1">Copy</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(deck, index) in decklists" :key="index">
              <td><i :class="getFormatClass(deck.format)"></i></td>
              <td>{{ deck.deckName }}</td>
              <td>
                <button
                  class="btn btn-light btn-sm"
                  v-on:click="copyToClipboard(deck.deckName, deck.deckList)"
                >
                  <i class="fas fa-clipboard"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script>
import backend from "../apis/backend";
import { useToast } from "vue-toastification";
export default {
  name: "Decklists",
  props: {},
  setup() {
    // Get toast interface
    const toast = useToast();
    return { toast };
  },
  data() {
    return {
      filter: "all",
    };
  },
  methods: {
    loadDeckLists() {
      backend.getDeckLists().then((response) => {
        this.decklists = response.data.deckLists;
      });
    },
    copyToClipboard(key, value) {
      navigator.clipboard.writeText(value);
      this.toast.success(`decklist ${key} copied to clipboard`, {
        timeout: 2000,
      });
    },
    getFormatClass(format)
    {
      return 'pkmn-format pkmn-'+format.toLowerCase()
    }
  },
  computed: {
    decklists() {
      if (this.filter !== "all") {
        return this.$store.getters.getDeckListsByFormat(this.filter);
      } else {
        return this.$store.getters.allDeckLists;
      }
    },
    formats() {
      return this.$store.getters.formats;
    },
  },
  mounted() {
    this.$store.dispatch("loadDeckLists");
  },
};
</script>
<style>
.pkmn-format {
  
  height: 31px;
  width: 31px;
  display: block;
}
.pkmn-expanded {
  background: url(../assets/expanded.png);
  background-size: 31px 31px;
}
.pkmn-std_2014_15 {
  background: url(../assets/std15.png);
  background-size: 31px 31px;
}.pkmn-std_2015_16 {
  background: url(../assets/std16.png);
  background-size: 31px 31px;
}
.pkmn-std_2016_17 {
  background: url(../assets/std17.png);
  background-size: 31px 31px;
}
.pkmn-std_2017_18 {
  background: url(../assets/std18.png);
  background-size: 31px 31px;
}
.pkmn-std_2018_19 {
  background: url(../assets/std19.png);
  background-size: 31px 31px;
}
.pkmn-std_2019_20 {
  background: url(../assets/std20.png);
  background-size: 31px 31px;
}
.pkmn-std_2020_21 {
  background: url(../assets/std21.png);
  background-size: 31px 31px;
}
.pkmn-std_2021_22 {
  background: url(../assets/std22.png);
  background-size: 31px 31px;
}

.table > tbody > tr > td {
  vertical-align: middle;
}
.table-wrapper {
  height:75vh;
  overflow:scroll;
  overflow-x: hidden;
}
</style>
