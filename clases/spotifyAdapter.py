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


    def get_token(self):
        username =  self.get_username()
        return util.prompt_for_user_token(username=username,scope='user-library-read',client_id='26501fd392cc4de19bb49aa6300002ae',client_secret='30a58c910ced414b92aa5dc707f8ccf5',redirect_uri='https://villegabriel.github.io/pruebaSoporte/')

    def get_username(self):
        return 'listpy'

    def search(self, name):
        token=util.prompt_for_user_token(username='listpy',scope='user-library-read',client_id='26501fd392cc4de19bb49aa6300002ae',client_secret='30a58c910ced414b92aa5dc707f8ccf5',redirect_uri='https://villegabriel.github.io/pruebaSoporte/')
        sp = spotipy.Spotify(auth=token)
        return sp.search(name,2)

    def adapt_to_autocomplete(self, tracks):
        lista = []
        class Aux:
            def serialize(self):
                return {
                    'id': self.id,
                    'value': self.value
                }
        for l in tracks['tracks']['items']:
            o = Aux()
            o.id = l['id']
            o.value= l['name']
            lista.append(o)
        return lista

    def get_user_saved_tracks(self, token,offset):
        sp = spotipy.Spotify(auth=token)
        result = sp.current_user_saved_tracks(5,offset)
        return result['items']

    def current_user_saved_tracks_add(self, token, ids):
        sp = spotipy.Spotify(auth=token)
        result = sp.current_user_saved_tracks_add(ids)
        return result

    def user_playlist_add_tracks(self, token, username, plid, ids):
        sp = spotipy.Spotify(auth=token)
        #sp.trace = False
        results = sp.user_playlist_add_tracks(username, plid, ids)
        return results

    def create_playlist(self, username, plname, token):
        sp = spotipy.Spotify(auth=token)
        result = sp.user_playlist_create(username, plname, public=True, description='Lista creada por Votaapp')
        return result
