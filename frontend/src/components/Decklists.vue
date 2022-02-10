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
            <td><i :class="deck.format"></i></td>
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
      <!--ul class="list-group">
        <li
          class="list-group-item justify-content-between d-flex"
          v-for="(deck, index) in decklists"
          :key="index"
        >
          <i :class="deck.format"></i>
          {{ deck.deckName }}          
          <button
            class="btn btn-light"
            v-on:click="copyToClipboard(deck.deckName, deck.deckList)"
          >
            <i class="fas fa-clipboard"></i>
          </button>
        </li>
      </ul-->
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
.Expanded {
  background: url(../assets/expanded.png);
  background-size: 20px 20px;
  height: 20px;
  width: 20px;
  display: block;
}
.table > tbody > tr > td {
  vertical-align: middle;
}
</style>
