from datetime import datetime
import mimetypes
from sre_constants import SUCCESS
from urllib import request, response
from flask import Flask, jsonify, send_from_directory, request, Response, json
from flask_cors import CORS
from os import path, listdir
import parseDecklist
from deck import DeckUnvalidCardError


# configuration
DEBUG = True
DIST_DIRECTORY="frontend/dist"

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.static_folder=path.join(DIST_DIRECTORY,'static')
app.static_url_path="static"

# enable CORS
CORS(app)


# sanity check route
@app.route('/', methods=['GET'])
def index():
    return send_from_directory(DIST_DIRECTORY, 'index.html')

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(DIST_DIRECTORY, 'favicon.ico')

@app.route('/adddecklist', methods=['POST'])
def addDeckList():

    response = None
    
    if "deckList" in request.json and "deckName" in request.json and "format" in request.json:
        deckName = datetime.now().strftime("%Y%m%d_%H%M%S")
        try:
            deck = parseDecklist.parseTCGODecklist(request.json["deckName"],request.json["deckList"],request.json["format"])
            path = deck.exportToTCGO()
            response = Response(f"{{\"location\": \"{path}\"}}", status=201, mimetype='application/json')
            resp = jsonify(success=True)
        except DeckUnvalidCardError :
            response = Response("{\"error\": \"deck is invalid\"}", status=422, mimetype='application/json')          
        
    else:
        response = Response("{\"error\": \"request is invalid, body syntax is {{deckList:'',deckName:'',format:''}}\"}", status=400, mimetype='application/json')
    return response

@app.route('/getdecklists', methods=['GET'])
def getDeckLists():
    deckLists = {}
    if not path.isdir("Export"):
        print("Please Create the Export folder")
    else:
        for file in listdir("Export/Expanded"):
            with open( f"Export/Expanded/{file}", "r", encoding="utf-8") as tcgolist:
                contents = tcgolist.read()
                print(contents)
                deckLists.update({file.replace(".txt","") : contents})
    response = Response(f"{{\"deckLists\": {json.dumps(deckLists)}}}", status=200, mimetype="application/json")
    return response

    



if __name__ == '__main__':
    app.run()