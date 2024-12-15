import tkinter as tk
from PIL import ImageTk, Image
from ObjetosPersonas.Artista import Artista_usados
from ObjetosPersonas.Persona import Persona
from ObjetosPersonas.Solicitante import Solicitante_usados
from ListaSimple.ListaSimple import ListaSimple
from Funciones.ArtistaFuncion import ArtistaFucnion
from PIL import Image, ImageTk

artista_1 = ArtistaFucnion()

def verificar_login():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if usuario == "A" and contrasena == "A":
        ventana_admin()
        
    elif usuario.startswith("AR"):
        ventana_artista()
    elif usuario.startswith("IP"):
        ventana_solicitante()
    else:
        label_error.config(text="Usuario o contraseña incorrectos.")

def ventana_admin():
    ventana_login.withdraw()  # Oculta la ventana de inicio de sesión
    ventana_admin = tk.Toplevel()  # Crea una nueva ventana
    ventana_admin.title("Módulo de Administrador")
    ventana_admin.geometry("1000x500")  # Ajusta las dimensiones según tus necesidades

    # Agrega un Frame que cubra todo el espacio disponible en la ventana
    frame = tk.Frame(ventana_admin, bg="#007bff")  # azul claro
    frame.pack(fill="both", expand=True)

    # Agrega los demás elementos dentro del Frame
    label_admin = tk.Label(frame, text="Bienvenido, Administrador!", bg="#007bff")
    label_admin.pack()

    label_REPORTE = tk.Label(frame, text="REPORTE", font=("Arial", 14), bg="#007bff")
    label_REPORTE.place(relx=0.7, rely=0.2, anchor="center")
    
    # Crea un cuadro o contenedor debajo del label "REPORTE"
    cuadro_reporte = tk.Frame(frame, bg="#ffffff", width=400, height=200)  # establece el fondo en blanco
    cuadro_reporte.place(relx=0.5, rely=0.3, anchor="center")

    # Crea un label para mostrar la imagen
    label_imagen = tk.Label(cuadro_reporte, bg="#ffffff")  # establece el fondo en blanco
    label_imagen.pack(fill="both", expand=True)
    

    boton1 = tk.Button(frame, text="Cargar Solicitantes", width=20, height=2, bg="orange")
    boton1.place(x=50, y=50)  # Posición en x=50, y=50

    boton2 = tk.Button(frame, text="Ver Solicitantes", width=20, height=2, bg="orange")
    boton2.place(x=50, y=100)  # Posición en x=50, y=100
    
    # Crea un cuadro o contenedor debajo del label "REPORTE"
    cuadro_reporte = tk.Frame(frame, bg="#ffffff", width=400, height=200)  # establece el fondo en blanco
    cuadro_reporte.place(relx=0.5, rely=0.3, anchor="center")

    # Crea un label para mostrar la imagen
    label_imagen = tk.Label(cuadro_reporte, bg="#ffffff")  # establece el fondo en blanco
    label_imagen.pack(fill="both", expand=True)

    # Función para mostrar la imagen
    def mostrar_imagen():
        imagen = Image.open("ListaSimple/listaSimple.png")
        imagen = imagen.resize((800, 300))  # Redimensiona la imagen a 400x200
        imagen = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(frame, image=imagen)
        label_imagen.image = imagen  # para evitar que la imagen se elimine
        label_imagen.place(x=220, y=120)  # Posiciona la imagen en x=300, y=200

    # Agrega el botón para mostrar la imagen
    boton3 = tk.Button(frame, text="Ver Artistas", width=20, height=2, bg="orange", command=lambda: [artista_1.mostrar_artistas(), mostrar_imagen()])
    boton3.place(x=50, y=150)  # Posición en x=50, y=150

    boton4 = tk.Button(frame, text="Cargar Artistas", width=20, height=2, bg="orange",command=artista_1.agregarArtistas)
    boton4.place(x=250, y=50)  # Posición en x=50, y=150

    boton_cerrar = tk.Button(frame, text="Cerrar", command=lambda: cerrar_ventana(ventana_admin), bg="red", fg="white")
    boton_cerrar.place(x=600, y=440)
    # boton_cerrar.pack()



def ventana_artista():
    ventana_login.withdraw()  # Oculta la ventana de inicio de sesión
    ventana_artista = tk.Toplevel()  # Crea una nueva ventana
    ventana_artista.title("Módulo de Artista")
    label_artista = tk.Label(ventana_artista, text="Bienvenido, Artista!")
    label_artista.pack()
    boton_cerrar = tk.Button(ventana_artista, text="Cerrar", command=lambda: cerrar_ventana(ventana_artista))
    boton_cerrar.pack()

def ventana_solicitante():
    ventana_login.withdraw()  # Oculta la ventana de inicio de sesión
    ventana_solicitante = tk.Toplevel()  # Crea una nueva ventana
    ventana_solicitante.title("Módulo de Solicitante")
    label_solicitante = tk.Label(ventana_solicitante, text="Bienvenido, Solicitante!")
    label_solicitante.pack()
    boton_cerrar = tk.Button(ventana_solicitante, text="Cerrar", command=lambda: cerrar_ventana(ventana_solicitante))
    boton_cerrar.pack()

def cerrar_ventana(ventana):
    ventana.destroy()  # Cierra la ventana actual
    ventana_login.deiconify()  # Muestra la ventana de inicio de sesión

# Ventana principal
ventana_login = tk.Tk()
ventana_login.title("IPCArt-Studio")
ventana_login.geometry("800x600") # Tamaño de la ventana

# Etiquetas
label_usuario = tk.Label(ventana_login, text="Usuario:")
label_contrasena = tk.Label(ventana_login, text="Contraseña:")
label_error = tk.Label(ventana_login, text="", fg="red")

# Campos de entrada
entry_usuario = tk.Entry(ventana_login)
entry_contrasena = tk.Entry(ventana_login, show="*")

# Botón de login
#boton_login = tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_login)
boton_login = tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_login, width=20, height=2,bg="orange")

# Layout
label_usuario.pack()
entry_usuario.pack()
label_contrasena.pack()
entry_contrasena.pack()
boton_login.pack()
label_error.pack()

ventana_login.mainloop()