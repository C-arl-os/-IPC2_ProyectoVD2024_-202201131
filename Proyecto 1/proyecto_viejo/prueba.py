from ObjetosPersonas.Artista import Artista_usados
from ObjetosPersonas.Persona import Persona
from ObjetosPersonas.Solicitante import Solicitante_usados
from ListaSimple.ListaSimple import ListaSimple
from Funciones.ArtistaFuncion import ArtistaFucnion

# Inicializar la lista
lesta = ListaSimple()
artista_1 = ArtistaFucnion()

def añadirArtista():
    # Crear un nuevo artista
    artistas = Artista_usados("123", "ipc", "carlos", "carlos@", "12341", "djcarlos", "el mejor dj")
    lesta.insertar(artistas)
    print("Artista añadido correctamente.")

def mostrarArtistas():
    # Aquí puedes implementar la lógica para mostrar los artistas en la lista
    # Por ejemplo, si tu clase ListaSimple tiene un método para listar elementos
    print("Artistas en la lista:")
    for artista in lesta:  # Asumiendo que ListaSimple es iterable
        print(artista)

def main():
    while True:
        print("\nMini Menú:")
        print("1. Añadir Artista")
        print("2. Mostrar Artistas")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            artista_1.agregarArtistas()
        elif opcion == "2":
            artista_1.mostrar_artistas()
            #lesta.imprimirLista()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()