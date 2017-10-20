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

@app.route('/test')
def test():
    sp = sa.SpotifyAdapter()
    a = sp.get_all_playlists_from_user(sp.get_token(sp.get_username()), sp.get_username())
    html = ''
    for pl in a['items']:
        html += pl['name'] + '<br>'
    return a['name']

@app.route('/tracks')
def tracks():
    sp = sa.SpotifyAdapter()
    b = sp.get_all_playlists_from_user(sp.get_token(sp.get_username()), sp.get_username())
    a = sp.get_all_tracks_from_playlist(sp.get_token(sp.get_username()), sp.get_username(), b)
    html = ''
    for pl in a['items']:
        html += pl['track']['name'] + '<br>'
    return html

app.run(debug=1)
