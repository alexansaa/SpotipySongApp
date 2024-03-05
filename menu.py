
def obtener_artistas(nombre_artista):
    # Implementa la lógica para obtener los artistas que coinciden con el nombre
    pass

def obtener_albumes(nombre_artista):
    # Implementa la lógica para obtener los álbumes de un artista
    pass

def obtener_canciones(nombre_album):
    # Implementa la lógica para obtener las canciones de un álbum
    pass

def obtener_bytestream(nombre_cancion):
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
