import axios from 'axios'

var headers = null

if (process.env.NODE_ENV == 'development') {
    headers = { 'Access-Control-Allow-Origin': '*' }
    console.log(headers)
}

console.log(process.env.VUE_APP_NODE_ENV)
console.log(process.env.VUE_APP_BACKEND_URL)

const instance = axios.create({
    baseURL: process.env.VUE_APP_BACKEND_URL,
    timeout: 1000,
    headers: headers
});


export default {

    async addDecklist(deckList, deckName, format) {
        return instance
            .post("adddecklist", {
                deckName: deckName,
                deckList: deckList,
                format: format
            })
    },
    async getDeckLists() {
        return instance
            .get("getdecklists")
    },
    async getDeckList(deckList) {
        return instance
            .get(`getdecklist/${deckList}`)
    }

}

