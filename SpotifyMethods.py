import spotipy
from spotipy.oauth2 import SpotifyOAuth

authScopes = {
    "default": "user-library-read"
}

def authFlow(scope):
    # scope = "user-library-read"
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def userSavedTracks(spotipyObj):
    results = spotipyObj.current_user_saved_tracks()

    print(results)

    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

if __name__=="__main__":
    print("Auth Flow")
    sp = authFlow(authScopes["default"])
    userSavedTracks(sp)

    