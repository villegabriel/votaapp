from spotipy import util
from flask import *
import spotipy
import clases.spotifyAdapter as sa

app = Flask(__name__)
@app.route('/')
def hola():
    sp = sa.SpotifyAdapter()
    a = sp.get_random_tracks_from_user_playlist('Esto es muy facil',5, sp.get_token(sp.get_username()), sp.get_username())
    html = ''
    for tema in a:
        html += tema['track']['name'] + '<br>'
    return html

app.run(debug=1)
