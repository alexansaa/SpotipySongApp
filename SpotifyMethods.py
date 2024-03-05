import urllib.parse
import spotipy
from spotipy.oauth2 import SpotifyOAuth

authScopes = {
    "default": "user-library-read"
}

queryType = {
    1: "artist",
    2: "album",
    3: "track",
    4: "playlist",
    5: "show",
    6: "episode",
    7: "audiobook"
}

def authFlow(scope):
    # scope = "user-library-read"
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def userSavedTracks(spotipyObj):
    results = spotipyObj.current_user_saved_tracks()

    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

def search(query, myQType, limit, spotipyObj):
    # formatedQuery = "artist:" + urllib.parse.quote(query)
    formatedQuery = urllib.parse.quote(query)

    return spotipyObj.search(formatedQuery, limit, 0, queryType[myQType], None)

def album_tracks(album_id, sp):
    return sp.album_tracks(album_id, 50, 0, None)

def track_info(track_id, sp):
    return sp.track(track_id, None)

if __name__=="__main__":
    print("Auth Flow")
    sp = authFlow(authScopes["default"])
    # userSavedTracks(sp)
    artists = search("Heroes del Silencio", 2, 10,sp)

    