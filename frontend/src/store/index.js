import { createStore } from 'vuex'
import backend from '../apis/backend'

export default createStore({
  state: {
    decklists: {},
  },
  getters: {
    formats(state) {
      let formats = []
      for (const [format] of Object.entries(state.decklists)) {
        formats.push(format)
      }
      return formats
    },
    allDeckLists(state) {
      let allDeckLists = []
      for (const [format, decks] of Object.entries(state.decklists)) {
        for (const [key, value] of Object.entries(decks)) {
          const deck = { deckName: key, deckList: value, format: format }
          allDeckLists.push(deck)
        }
      }
      return allDeckLists
    },
    getDeckListsByFormat: (state) => (formatFilter) => {
      let filteredDeckLists = []
      for (const [format, decks] of Object.entries(state.decklists)) {
        console.log(format)
        if (format === formatFilter) {
          for (const [key, value] of Object.entries(decks)) {
            const deck = { deckName: key, deckList: value, format: format }
            filteredDeckLists.push(deck)
          }
        }
      }
      return filteredDeckLists
    }
  },
  mutations: {
    updateDeckLists(state, newDeckLists) {
      state.decklists = newDeckLists
    }
  },
  actions: {
    loadDeckLists(context) {
      backend.getDeckLists().then(response => {
        context.commit('updateDeckLists', response.data.deckLists)
      })
    }
  },
  modules: {
  }
})
