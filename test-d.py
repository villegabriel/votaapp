import spotipy
from spotipy import util
from flask import Flask, render_template, jsonify, request
from spotipy import oauth2
import jinja2
from flask_bootstrap import Bootstrap
from clases import spotifyAdapter as sa
from threading import Timer


app = Flask(__name__)

class Test:
    def serialize(self):
        return {
            'id': self.id,
            'value': self.value
        }
    pass

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    @app.route("/searchSongService",methods=['POST'])
    def searchSongService():
        sp = sa.SpotifyAdapter()
        if request.form['operation'] == "searchSong":
            listToReturn = sp.adapt_to_autocomplete(sp.search(request.form['term']))
            prepared = jsonify(results =[result.serialize() for result in listToReturn])
            return prepared
        elif request.form['operation'] == "getUserTracks":
            offset = request.form['offset']
            return jsonify(sp.get_user_saved_tracks(sp.get_token(),offset))
        elif "addSongToMyMusic" == request.form['operation']:
            id = request.form['id']
            sp.current_user_saved_tracks_add(sp.get_token(), [id])
            return ''
        elif "getAllPlaylists" == request.form['operation']:
            return jsonify(sp.get_all_playlists_from_user(sp.get_token(), sp.get_username()))
        elif "createPlaylist" == request.form['operation']:
            return jsonify(sp.create_playlist(sp.get_username(), request.form['plname'] , sp.get_token()))
        elif "addTracksToPlaylist" == request.form['operation']:
            return jsonify(sp.user_playlist_add_tracks(sp.get_token(), sp.get_username(), request.form['plid'], request.form['ids']))

    @app.route("/")
    def root():
        sp = sa.SpotifyAdapter()
        playlists = sp.get_all_playlists_from_user(sp.get_token(), sp.get_username())
        current_song = sp.get_current_playing()
        t = Timer((current_song['item']['duration_ms'] - current_song['progress_ms'])/1000, test_timer)
        t.start()
        return render_template("home.html", playlists=playlists['items'])

    def test_timer():
        print('termino la cancion')

    return app
create_app().run(debug=1)


