import spotipy
from spotipy import util
from flask import Flask, render_template, jsonify, request
from spotipy import oauth2
import jinja2


app = Flask(__name__)

@app.route("/")
def root():
#    username = 'listpy'
#    scope = 'user-library-read'
#    token = util.prompt_for_user_token(username,
#        scope,
#        client_id='26501fd392cc4de19bb49aa6300002ae',
#        client_secret='30a58c910ced414b92aa5dc707f8ccf5',
#        redirect_uri='http://damianciancio.github.io')
#    return token
    return render_template("home.html",mensaje="hola", cuerpo='testing')
@app.route("/searchSongService",methods=['POST'])
def searchSongService():
    listToReturn = []
    listToValidate = []
    obj1 = Test()
    obj1.id = 1
    obj1.value = "ga"
    obj2 = Test()
    obj2.id = 1
    obj2.value = "to"
    listToValidate.append(obj1)
    listToValidate.append(obj2)
    for candidate in listToValidate:
        if candidate.value.startswith(request.form['term']):
            listToReturn.append(candidate)
    return jsonify(results =[result.serialize() for result in listToReturn])


class Test:
    def serialize(self):
        return {
            'id': self.id,
            'value': self.value
        }
    pass
app.run(debug=1)
