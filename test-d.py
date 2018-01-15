import spotipy
import tweepy
from spotipy import util
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from spotipy import oauth2
import jinja2
from flask_bootstrap import Bootstrap
from clases import spotifyAdapter as sa
from threading import Timer

sp_oauth = SpotifyOAuth('26501fd392cc4de19bb49aa6300002ae', '30a58c910ced414b92aa5dc707f8ccf5','http://127.0.0.1:5000/authenticateSpotify',scope='user-read-currently-playing playlist-modify-public playlist-modify-private user-library-modify user-library-read')

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
    app.secret_key = 'supersecretkey'
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
        #current_song = sp.get_current_playing()
        #t = Timer((current_song['item']['duration_ms'] - current_song['progress_ms'])/1000, test_timer)
        #t.start()
        return render_template("home.html", playlists=playlists['items'])

    def test_timer():
        print('termino la cancion')

    @app.route('/twitterAuthenticate')
    def twitterAuthenticate():
        oauth = tweepy.OAuthHandler('qcwrmAocu3cuCT5D8iMB3DdWI', 'tUUZ1s56ry3yVrAhrOs7gG7R6VDQ2yhaKIDBekeMvOOXLSoLSD')
        try:
            auth_url = oauth.get_authorization_url(True)
        except Exception as e:
            print(e)
        session['request_token'] = oauth.request_token
        return redirect(auth_url)

    @app.route('/twitterOk', methods=['GET','POST'])
    def twitterOk():
        verifier = request.args.get('oauth_verifier')
        oauth = tweepy.OAuthHandler('qcwrmAocu3cuCT5D8iMB3DdWI', 'tUUZ1s56ry3yVrAhrOs7gG7R6VDQ2yhaKIDBekeMvOOXLSoLSD')
        token = session['request_token']
        session['request_token'] = None
        oauth.request_token = token
        try:
            oauth.get_access_token(verifier)
        except tweepy.TweepError:
            print('Error, failed to get access token')

        session['access_key_tw'] = oauth.access_token
        session['access_secret_tw'] = oauth.access_token_secret
        return redirect(sp_oauth.get_authorize_url(None, True))

    @app.route('/authenticateSpotify')
    def authenticateSpotify():
        token_info = sp_oauth.get_cached_token()
        access_token = None
        if token_info:
            access_token = token_info
        else:
            code = request.args.get('code')
            if code:
                token_info = sp_oauth.get_access_token(code)
                access_token = token_info['access_token']
        if access_token:
            print ("Access token available! Trying to get user information...")
            sp = spotipy.Spotify(access_token)
            session["access_token_spotify"] = access_token
            return redirect(url_for('root'))
        else:
            return redirect(url_for('root'))

    return app
create_app().run(debug=1)


