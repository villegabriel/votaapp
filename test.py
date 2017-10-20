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


a = get_all_playlists_from_user(get_token(get_username()), get_username())

b = get_all_tracks_from_playlist(get_token(get_username()), get_username(), a)

for a in b['items']:
    print a['track']['name']
