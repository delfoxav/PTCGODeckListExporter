<template>
  <div class="import">
    <form @submit.prevent="submitForm">
      <div class="form-group m-3">
        <label>Deck Name</label>
        <input type="text" class="form-control" v-model="deckName" />
      </div>
      <div class="form-group m-3">
        <label>Format</label>
        <select class="form-select" v-model="format">
          <option disabled value="">Please select one</option>
          <option v-for="(i, index) in formats" :key="index">{{ i }}</option>
        </select>
      </div>
      <div class="form-group m-3">
        <label>Decklist</label>
        <textarea
          rows="30"
          cols="45"
          type="text"
          class="form-control"
          v-model="deckList"
        />
      </div>
      <div class="form-group m-3">
        <button type="submit" class="btn btn-primary">Import a deck</button>
      </div>
    </form>
  </div>
</template>
<script>
import backend from "../apis/backend";
import { useToast } from "vue-toastification";

export default {
  name: "ImportDeck",
  setup() {
    // Get toast interface
    const toast = useToast();
    return { toast };
  },
  data() {
    return {
      deckList: "",
      deckName: "",
      format: "",
      formats: ["Standard", "Expanded"],
    };
  },
  methods: {
    submitForm() {
      backend
        .addDecklist(this.deckList, this.deckName, this.format)
        .then((response) => {
          if (String(response.status) == "201") {
            this.toast.success(
              `decklist saved under ${response.data.location}`,
              { timeout: 2000 }
            );
          }
          this.deckName = "";
          this.deckList = "";
        })
        .catch((error) => {
          if (String(error.response.status) == "422") {
            this.toast.error(`${error.response.data.error}`, { timeout: 2000 });
          }
        });
    },
  },
};
</script>
<style scoped>
textarea {
  resize: none;
  overflow: scroll;
}
</style>