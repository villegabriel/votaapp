from spotipy import util
import spotipy
from numpy import random
from flask import *

def get_token(username):
        return util.prompt_for_user_token(username=username,scope='user-library-read',client_id='26501fd392cc4de19bb49aa6300002ae',client_secret='30a58c910ced414b92aa5dc707f8ccf5',redirect_uri='https://villegabriel.github.io/pruebaSoporte/')

def get_username():
        return 'listpy'

def get_all_playlists_from_user(token, username):
    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for pl in playlists['items']:
            if pl['name']=='Esto es muy facil':
                return pl

def get_all_tracks_from_playlist(token, username, pl):
        if token:
            sp = spotipy.Spotify(auth=token)
            tracks = sp.user_playlist_tracks(username, pl['id'])
            print tracks
            return tracks


def get_user_tracks():
    username='listpy'
    token=util.prompt_for_user_token(username='listpy',scope='user-library-read',client_id='26501fd392cc4de19bb49aa6300002ae',client_secret='30a58c910ced414b92aa5dc707f8ccf5',redirect_uri='https://villegabriel.github.io/pruebaSoporte/')
    if token:
        sp = spotipy.Spotify(auth=token)
        tracks = sp.current_user_saved_tracks(10)

        return tracks

            #else:
             #   print "Can't get token for", username
def prepare_to_combo(tracks):
    lista = {}
    for item in tracks['items']:
        lista[item['track']['id']] = item['track']['name']
        print item['track']['name']
    return lista


def search( name):
    token=util.prompt_for_user_token(username='listpy',scope='user-library-read',client_id='26501fd392cc4de19bb49aa6300002ae',client_secret='30a58c910ced414b92aa5dc707f8ccf5',redirect_uri='https://villegabriel.github.io/pruebaSoporte/')
    sp = spotipy.Spotify(auth=token)
    return sp.search(name)

def adapt_to_autocomplete(tracks):
    lista = []
    class Prueba:
        pass
    for l in tracks['tracks']['items']:
        o = Prueba()
        o.id = l['id']
        o.value= l['name']
        lista.append(o)
    return lista

