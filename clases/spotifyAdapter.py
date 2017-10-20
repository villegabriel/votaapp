from spotipy import util
import spotipy
from numpy import random
from spotipy import oauth2

class SpotifyAdapter:

    def get_all_playlists_from_user(self, token, username):
        if token:
            sp = spotipy.Spotify(auth=token)
            playlists = sp.user_playlists(username)
            return playlists

    def get_all_tracks_from_playlist(self, token, username, pl):
        if token:
            sp = spotipy.Spotify(auth=token)
            tracks = sp.user_playlist_tracks(username, pl['id'])
            return tracks

    def get_random_tracks_from_user_playlist(self,list, size, token, username):
        if token:
            sp = spotipy.Spotify(auth=token)
            playlists = sp.user_playlists(username)
            for pl in playlists['items']:
                if pl['name']==list:
                    results = sp.user_playlist(username, pl['id'], fields="tracks")
                    temas = results['tracks']['items']
                    return random.choice(temas, size)


    def get_token(self, username):
        return util.prompt_for_user_token(username=username,scope='user-library-read',client_id='26501fd392cc4de19bb49aa6300002ae',client_secret='30a58c910ced414b92aa5dc707f8ccf5',redirect_uri='https://villegabriel.github.io/pruebaSoporte/')

    def get_username(self):
        return 'listpy'

