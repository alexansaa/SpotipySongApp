import SpotifyMethods
import webbrowser

sp = None

authScopes = {
    "default": "user-library-read"
}

def test():
    # Implementa la lógica para obtener los artistas que coinciden con el nombre
    # global sp
    SpotifyMethods.userSavedTracks(sp)
    pass 

def obtener_artistas(nombre_artista):
    # Implementa la lógica para obtener los artistas que coinciden con el nombre
    response = SpotifyMethods.search(nombre_artista,1,10,sp)
    # print(response)
    for artist in response['artists']['items']:
        print(artist['name'])
    pass

def obtener_albumes(nombre_artista):
    # Implementa la lógica para obtener los álbumes de un artista
    response = SpotifyMethods.search(nombre_artista,2,10,sp)
    for album in response['albums']['items']:
        print(album['name'] + "  " + album['id'])
    pass

def obtener_canciones(album_id):
    # Implementa la lógica para obtener las canciones de un álbum
    response = SpotifyMethods.album_tracks(album_id, sp)
    for item in response['items']:
        print(item['name'] + "  " + item['id'])

def obtener_bytestream(nombre_cancion):
    response = SpotifyMethods.track_info(nombre_cancion, sp)
    preview_url = response['preview_url']
    if preview_url:
        webbrowser.open(preview_url)  # Opens the preview URL in a web browser
        # Or use a suitable library to play audio from the URL, for example:
        # subprocess.run(['vlc', '--play-and-exit', preview_url])  # Opens with VLC player
    else:
        print("No preview available for this track.")
    
    # Implementa la lógica para obtener el bytestream de una canción
    pass

def mostrar_menu():
    print("Menú:")
    print("1. Buscar artistas por nombre")
    print("2. Mostrar álbumes de un artista")
    print("3. Mostrar canciones de un álbum")
    print("4. Obtener bytestream de una canción")
    print("0. Salir")

def main():
    global sp
    sp = SpotifyMethods.authFlow(authScopes["default"])

    # test()

    while True:
        mostrar_menu()
        opcion = input("Ingresa el número de la opción que deseas: ")

        if opcion == "1":
            nombre_artista = input("Ingresa el nombre del artista: ")
            
            obtener_artistas(nombre_artista)

        elif opcion == "2":
            nombre_artista = input("Ingresa el nombre del artista: ")
            obtener_albumes(nombre_artista)

        elif opcion == "3":
            nombre_album = input("Ingresa el nombre del álbum: ")
            obtener_canciones(nombre_album)

        elif opcion == "4":
            nombre_cancion = input("Ingresa el nombre de la canción: ")
            obtener_bytestream(nombre_cancion)

        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Ingresa un número válido.")

if __name__ == "__main__":
    main()
