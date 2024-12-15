import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image, UnidentifiedImageError
import xml.etree.ElementTree as ET
# Importar Tkinter para obtener la ruta de los archivos XML
from tkinter import filedialog, messagebox


from clases.Artista import Artista
from clases.Imagen import Imagen
from clases.Solicitante import Solicitante
from clases.SolicitudCola import SolicitudCola
from clases.SolicitudPila import SolicitudPila
from estructuras.estructuras import (colaSolicitudes, id_logueado,
                                     listaArtistas, listaSolicitantes)
from estructuras.matrizDispersa.matrizDispersa import MatrizDispersa

# Declarar la variable global aquí
id_logueado = None

def verificar_login():
    global id_logueado  # Asegúrate de declarar que estás usando la variable global
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    
    if usuario == "a" and contrasena == "a":
        ventana_admin()
    elif usuario.startswith("ART-") and listaArtistas.loginUsuario(usuario, contrasena):
        id_logueado = usuario  # Asigna el ID del usuario logueado
        print(id_logueado)  # Esto debería imprimir el ID del usuario
        ventana_artista()
    elif usuario.startswith("IPC-") and listaSolicitantes.login(usuario, contrasena):
        id_logueado = usuario  # Asigna el ID del usuario logueado
        print(id_logueado)  # Esto debería imprimir el ID del usuario
        ventana_solicitante()
    else:
        label_error.config(text="Usuario o contraseña incorrectos.")
        

    """ 
    if usuario == "A" and contrasena == "A":
        ventana_admin()
    elif usuario.startswith("AR"):
        ventana_artista()
    elif usuario.startswith("IP"):
        ventana_solicitante()
    else:
        label_error.config(text="Usuario o contraseña incorrectos.")"""

def cerrar_ventana_y_mostrar(ventana_a_cerrar, ventana_a_mostrar):
    """
    Cierra una ventana específica y muestra otra ventana específica.
    """
    ventana_a_cerrar.destroy()  # Cierra la ventana actual
    ventana_a_mostrar.deiconify()  # Muestra la ventana solicitada

def ventana_admin():
    ventana_login.withdraw()  # Oculta la ventana de inicio de sesión
    ventana_admin = tk.Toplevel()  # Crea una nueva ventana
    ventana_admin.title("Módulo de Administrador")
    ventana_admin.geometry("1000x500")  # Ajusta las dimensiones según tus necesidades

    frame = tk.Frame(ventana_admin, bg="#007bff")  # Fondo azul claro
    frame.pack(fill="both", expand=True)

    label_admin = tk.Label(frame, text="Bienvenido, Administrador!", bg="#007bff")
    label_admin.pack()
    
    label_Reporte = tk.Label(frame, text="REPORTE", bg="#007bff", font=("Arial", 16, "bold"))
    label_Reporte.place(x=450, y=50)  # Coloca el label en la posición deseada

    boton1 = tk.Button(frame, text="Cargar Solicitantes", width=20, height=2, bg="orange", command=CargarSolicitantes)
    boton1.place(x=50, y=50)

    boton2 = tk.Button(frame, text="Ver Solicitantes", width=20, height=2, bg="orange", command=lambda: ver_solicitantes(ventana_admin))
    boton2.place(x=50, y=100)

    boton3 = tk.Button(frame, text="Ver Artistas", width=20, height=2, bg="orange", command=lambda: ver_artistas(ventana_admin))
    boton3.place(x=50, y=150)

    boton4 = tk.Button(frame, text="Cargar Artistas", width=20, height=2, bg="orange",command=CargarArtistas)
    boton4.place(x=250, y=50)

    boton_cerrar = tk.Button(frame, text="Cerrar", command=lambda: cerrar_ventana_y_mostrar(ventana_admin, ventana_login), bg="red", fg="white")
    boton_cerrar.place(x=600, y=440)

def ver_solicitantes(ventana_admin):
    # Generar la gráfica de solicitantes
    listaSolicitantes.graficar()

    # Cargar la imagen generada
    ruta_imagen = 'C:\\Users\\sanci\\Desktop\\proyectopracticas\\Proyecto 1\\Clase8\\reportes\\listaDoble.png'  # Asegúrate de que esta ruta sea correcta
    try:
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((1200, 200), Image.LANCZOS)  # Cambia ANTIALIAS por LANCZOS
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Si ya hay una imagen mostrada, la eliminamos
        for widget in ventana_admin.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("image") != "":
                widget.destroy()  # Elimina el label de la imagen anterior

        # Crear un label para mostrar la imagen
        label_imagen = tk.Label(ventana_admin, image=imagen_tk)
        label_imagen.image = imagen_tk  # Mantener una referencia a la imagen
        label_imagen.place(x=200, y=100)  # Colocar la imagen en una posición que no estorbe a los botones

    except FileNotFoundError:
        messagebox.showerror("Error", f"No se pudo encontrar la imagen en la ruta: {ruta_imagen}")
    except UnidentifiedImageError:
        messagebox.showerror("Error", f"No se pudo identificar la imagen en la ruta: {ruta_imagen}")

def ver_artistas(ventana_admin):
    # Generar la gráfica de artistas
    listaArtistas.graficar()

    # Cargar la imagen generada
    ruta_imagen = 'C:\\Users\\sanci\\Desktop\\proyectopracticas\\Proyecto 1\\Clase8\\reportes\\listaSimple.png'  # Asegúrate de que esta ruta sea correcta
    try:
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((1200, 200), Image.LANCZOS)  # Cambia ANTIALIAS por LANCZOS
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Si ya hay una imagen mostrada, la eliminamos
        for widget in ventana_admin.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("image") != "":
                widget.destroy()  # Elimina el label de la imagen anterior

        # Crear un label para mostrar la imagen
        label_imagen = tk.Label(ventana_admin, image=imagen_tk)
        label_imagen.image = imagen_tk  # Mantener una referencia a la imagen
        label_imagen.place(x=200, y=100)  # Colocar la imagen en una posición que no estorbe a los botones

    except FileNotFoundError:
        messagebox.showerror("Error", f"No se pudo encontrar la imagen en la ruta: {ruta_imagen}")
    except UnidentifiedImageError:
        messagebox.showerror("Error", f"No se pudo identificar la imagen en la ruta: {ruta_imagen}")

    



#________________
def ventana_artista():
    global id_logueado
    
    ventana_login.withdraw()  # Oculta la ventana de inicio de sesión
    ventana_artista = tk.Toplevel()  # Crea una nueva ventana
    ventana_artista.title("Módulo de Artista")
    ventana_artista.geometry("1000x500")

    frame1 = tk.Frame(ventana_artista, bg="#FF5733")  # Fondo
    frame1.pack(fill="both", expand=True)

    label_artista = tk.Label(frame1, text="Bienvenido, Artista!", font=("Arial", 14), bg="#FF5733")
    label_artista.pack()
    
    id_global = id_logueado
    if colaSolicitudes.verPrimero() == None:
            print('---------------NO HAY SOLICITUDES------------')
    else:
            solicitud = colaSolicitudes.verPrimero()
            print(f'------------SOLICITUD ID: {solicitud.id}---------------')
            print(f'Ruta XML: {solicitud.ruta_xml}')
            print(f'Solicitante: {solicitud.id_solicitante}')
            print('------------------------------------------------')
            # Crear un Label para mostrar el ID y la longitud de las imágenes
            label_info = tk.Label(frame1, text=f"SOLICITUD ID: {solicitud.id}\n Ruta XML: {solicitud.ruta_xml}\nSolicitante: {solicitud.id_solicitante}", font=("Arial", 12))
            label_info.pack(pady=10)  # Usa pack para el label de información

    
    #____________________
    
    boton1 = tk.Button(frame1, text="Aceptar", width=20, height=2, bg="blue",command=AceptarSolicitud)
    boton1.place(x=50, y=50)

    boton2 = tk.Button(frame1, text="Ver Cola", width=20, height=2, bg="orange")
    boton2.place(x=50, y=150)

    boton3 = tk.Button(frame1, text="Imágenes Solicitadas", width=20, height=2, bg="orange")
    boton3.place(x=50, y=200)

    boton_cerrar = tk.Button(frame1, text="Cerrar", command=lambda: cerrar_ventana_y_mostrar(ventana_artista, ventana_login), bg="red", fg="white")
    boton_cerrar.pack()
#:::::::::funciones de artista::::::::::::
def aceptar_solicitudad_usu():
    colaSolicitudes.graficar()

def AceptarSolicitud():
    global id_logueado
    solicitud = colaSolicitudes.verPrimero()
    if solicitud == None:
        return
    #LO SACAMOS DE LA COLA
    solicitud_aceptada = colaSolicitudes.dequeue()
    #INSERTAN EN LA LISTA CIRCULAR
    listaArtistas.insertarProcesados(id_logueado,solicitud_aceptada)
    #GENERAMOS LA FIGURA
    matriz_figura = MatrizDispersa()
    #PARSEAR EL XML
    tree = ET.parse(solicitud_aceptada.ruta_xml)
    #Obtengo el elemento raiz
    root = tree.getroot()
    nombre_figura = ''
    for elemento in root:
        if elemento.tag == 'diseño':
            for pixel in elemento:
                fila = int(pixel.attrib['fila'])
                columna = int(pixel.attrib['col'])
                color = pixel.text
                matriz_figura.insertar(fila,columna,color)
        elif elemento.tag == 'nombre':
            nombre_figura = elemento.text

    
    #GRAFICAMOS
    ruta = matriz_figura.graficar(solicitud_aceptada.id)
    #creamos el nuevo objeto imagen para insertarlo a la lista doble del usuario
    nueva_imagen = Imagen(solicitud_aceptada.id,nombre_figura,ruta)
    #insertamos el objeto a la lista doble del usuario
    listaSolicitantes.insertarImagenUsuario(solicitud_aceptada.id_solicitante,nueva_imagen)

def ventana_galeria(ventana_solicitante):
    ventana_solicitante.withdraw()  # Oculta la ventana de solicitante
    ventana_galeria = tk.Toplevel()  # Crea la ventana galería
    ventana_galeria.title("Galería")
    ventana_galeria.geometry("900x500")

    frame_galeria = tk.Frame(ventana_galeria, bg="#FFE5B4")
    frame_galeria.pack(fill="both", expand=True)

    label_galeria = tk.Label(frame_galeria, text="Galería", font=("Arial", 18), bg="#FFE5B4")
    label_galeria.pack(pady=20)

    boton1 = tk.Button(frame_galeria, text="ANTERIOR", width=20, height=2, bg="silver")
    boton1.place(x=50, y=50)

    boton2 = tk.Button(frame_galeria, text="SIGUIENTE", width=20, height=2, bg="silver")
    boton2.place(x=700, y=50)
    
    boton_cerrar = tk.Button(
        frame_galeria,
        text="Cerrar",
        command=lambda: cerrar_ventana_y_mostrar(ventana_galeria, ventana_solicitante),
        bg="red",
        fg="white"
    )
    boton_cerrar.place(x=700,y=10)

def ventana_reporte(ventana_solicitante):
    global id_logueado
    print(id_logueado)
    solicitante:Solicitante = listaSolicitantes.buscar(id_logueado)
    imagen = None
    #print(len(solicitante.imagenes))
    if solicitante is None:
        print("No se encontró un solicitante con el ID:", id_logueado)
        return  # O maneja el error de otra manera
    else:
        print(len(solicitante.imagenes))
    print("::::::::::::::::::")
    if len(solicitante.imagenes) != 0:
        imagen:Imagen = solicitante.imagenes.primero.valor
        
    #:::::::::::::::::::::
    ventana_solicitante.withdraw()  # Oculta la ventana de solicitante
    ventana_reporte = tk.Toplevel()  # Crea la ventana reporte
    ventana_reporte.title("Solicitar")
    
    ventana_reporte.geometry("1000x500")

    frame_reporte = tk.Frame(ventana_reporte, bg="#D5F5E3")
    frame_reporte.pack(fill="both", expand=True)
    #::::::::::::::.
     # Obtener el ID y la longitud de las imágenes
    id_global = id_logueado  # ID del solicitante logueado
    num_imagenes = len(solicitante.imagenes)  # Longitud de las imágenes del solicitante

    # Crear un Label para mostrar el ID y la longitud de las imágenes
    label_info = tk.Label(frame_reporte, text=f"ID : {id_global}, Número de imágenes: {num_imagenes}", font=("Arial", 12))
    label_info.pack(pady=10)  # Usa pack para el label de información
    #____________________

    label_reporte = tk.Label(frame_reporte, text="Reporte", font=("Arial", 18), bg="#D5F5E3")
    label_reporte.pack(pady=20)
    
    boton1 = tk.Button(frame_reporte, text="Cargar Figura", width=20, height=2, bg="orange",command=CargarXMLFiguras)
    boton1.place(x=50, y=50)

    boton2 = tk.Button(frame_reporte, text="Solicitar", width=20, height=2, bg="orange",command=Solicitar)
    boton2.place(x=50, y=130)
    
    
        
    
    

    boton3 = tk.Button(frame_reporte, text="Ver Pila", width=20, height=2, bg="orange",command=lambda: graficar_pila_reporte(ventana_reporte))
    boton3.place(x=50, y=200)

    boton4 = tk.Button(frame_reporte, text="Ver lista", width=20, height=2, bg="orange",command=lambda:graficar_lista_doble(ventana_reporte))
    boton4.place(x=50, y=270)

    boton_cerrar = tk.Button(
        frame_reporte,
        text="Cerrar",
        command=lambda: cerrar_ventana_y_mostrar(ventana_reporte, ventana_solicitante),
        bg="red",
        fg="white"
    )
    boton_cerrar.place(x=900,y=10)
    
#____________________opciones

def graficar_lista_doble(ventana_reporte):
    global id_logueado
    solicitante: Solicitante = listaSolicitantes.buscar(id_logueado)
    if solicitante is None:
        print("No se encontró un solicitante con el ID:", id_logueado)
        return  # O maneja el error de otra manera
    solicitante.imagenes.graficar()
    
    # Cargar y mostrar la imagen
    ruta_imagen = r"C:\Users\sanci\Desktop\proyectopracticas\Proyecto 1\Clase8\reportes\listaDobleCircular.jpg"
    try:
        # Abrir la imagen
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((400, 200), Image.LANCZOS)  # Redimensionar la imagen a 400x400
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Crear un Label para mostrar la imagen
        label_image = tk.Label(ventana_reporte, image=imagen_tk)  # Usa la ventana de reporte
        label_image.image = imagen_tk  # Mantener una referencia a la imagen
        label_image.place(x=300,y=150)  # Empaquetar el Label de la imagen

    except FileNotFoundError:
        messagebox.showerror("Error", f"No se pudo encontrar la imagen en la ruta: {ruta_imagen}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    

def graficar_pila_reporte(ventana_reporte):
    global id_logueado
    solicitante: Solicitante = listaSolicitantes.buscar(id_logueado)

    if solicitante is None:
        print("No se encontró un solicitante con el ID:", id_logueado)
        return  # O maneja el error de otra manera

    # Generar la gráfica de la pila
    solicitante.pila.graficar()  # Asegúrate de que esta función genere la imagen en la ruta correcta

    # Cargar y mostrar la imagen
    ruta_imagen = r"C:\Users\sanci\Desktop\proyectopracticas\Proyecto 1\Clase8\reportes\pila.png"
    try:
        # Abrir la imagen
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((400, 200), Image.LANCZOS)  # Redimensionar la imagen a 400x400
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Crear un Label para mostrar la imagen
        label_image = tk.Label(ventana_reporte, image=imagen_tk)  # Usa la ventana de reporte
        label_image.image = imagen_tk  # Mantener una referencia a la imagen
        label_image.place(x=300,y=150)  # Empaquetar el Label de la imagen

    except FileNotFoundError:
        messagebox.showerror("Error", f"No se pudo encontrar la imagen en la ruta: {ruta_imagen}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def CargarXMLFiguras():
    global id_logueado
    ruta = filedialog.askopenfilename(title="Cargar Archivo", filetypes=(('Text files', '*.xml'), ('All files','*.*')))
    #PARSEAR EL XML
    tree = ET.parse(ruta)
    #Obtengo el elemento raiz
    root = tree.getroot()

    id = ''
    if root.tag == "figura":
        for elementos in root:
            if elementos.tag == "nombre":
                id = elementos.attrib["id"]
    
    nueva = SolicitudPila(id,ruta)
    listaSolicitantes.insertaraPilaUsuario(id_logueado,nueva)
    
def Solicitar():
    global id_logueado
    valorSacado = listaSolicitantes.sacardePilaUsuario(id_logueado)
    while valorSacado != None:
        nueva_solicitud = SolicitudCola(valorSacado.id,valorSacado.ruta_xml,id_logueado)
        colaSolicitudes.enqueue(nueva_solicitud)
        valorSacado = listaSolicitantes.sacardePilaUsuario(id_logueado)
        print("SE AÑADIO")


#VER PILA

#:::::::::::::::::::::::::::::.

def ventana_solicitante():
    ventana_login.withdraw()  # Oculta la ventana de inicio de sesión
    ventana_solicitante = tk.Toplevel()  # Crea una nueva ventana
    ventana_solicitante.title("Módulo de Solicitante")
    ventana_solicitante.geometry("500x500")

    frame1 = tk.Frame(ventana_solicitante, bg="#FF5733")  # Fondo
    frame1.pack(fill="both", expand=True)

    label_solicitante = tk.Label(frame1, text="Bienvenido, Solicitante!", bg="#FF5733")
    label_solicitante.pack(pady=10)

    boton1 = tk.Button(
        frame1,
        text="Galería",
        width=20,
        height=2,
        bg="blue",
        command=lambda: ventana_galeria(ventana_solicitante)
    )
    boton1.place(x=50, y=50)

    boton2 = tk.Button(
        frame1,
        text="Reporte",
        width=20,
        height=2,
        bg="orange",
        command=lambda: ventana_reporte(ventana_solicitante)
    )
    boton2.place(x=230, y=50)

    boton_cerrar = tk.Button(
        frame1,
        text="Cerrar",
        command=lambda: cerrar_ventana_y_mostrar(ventana_solicitante, ventana_login),
        bg="red",
        fg="white"
    )
    boton_cerrar.place(x=200,y=200)

def cerrar_ventana(ventana):
    ventana.destroy()
    ventana_login.deiconify()
#funcion codigo 
def CargarSolicitantes():
    ruta = filedialog.askopenfilename(title="Cargar Archivo", filetypes=(('Text files', '*.xml'), ('All files','*.*')))
    
    #PARSEAR EL XML
    tree = ET.parse(ruta)
    #Obtengo el elemento raiz
    root = tree.getroot()

    if root.tag == "solicitantes":
        for solicitante in root:
            id = solicitante.attrib["id"]
            pwd = solicitante.attrib["pwd"]
            nombre = ''
            correo = ''
            telefono = ''
            direccion = ''
            for hijo in solicitante:
                if hijo.tag == "NombreCompleto":
                    nombre = hijo.text
                elif hijo.tag == "CorreoElectronico":
                    correo = hijo.text
                elif hijo.tag == "NumeroTelefono":
                    telefono = hijo.text
                elif hijo.tag == "Direccion":
                    direccion = hijo.text
            nuevo_solicitante = Solicitante(id,pwd,nombre,correo,telefono,direccion)
            listaSolicitantes.insertar(nuevo_solicitante)

def CargarArtistas():#-----------------------------
    ruta = filedialog.askopenfilename(title="Cargar Archivo", filetypes=(('Text files', '*.xml'), ('All files','*.*')))
    
    #PARSEAR EL XML
    tree = ET.parse(ruta)
    #Obtengo el elemento raiz
    root = tree.getroot()

    if root.tag == "Artistas":
        for artista in root:
            id = artista.attrib["id"]
            pwd = artista.attrib["pwd"]
            nombre = ''
            correo = ''
            telefono = ''
            especialidades = ''
            notas = ''
            for hijo in artista:
                if hijo.tag == "NombreCompleto":
                    nombre = hijo.text
                elif hijo.tag == "CorreoElectronico":
                    correo = hijo.text
                elif hijo.tag == "NumeroTelefono":
                    telefono = hijo.text
                elif hijo.tag == "Especialidades":
                    especialidades = hijo.text
                elif hijo.tag == "NotasAdicionales":
                    notas = hijo.text
            nuevo_artista = Artista(id,pwd,nombre,correo,telefono,especialidades,notas)
            listaArtistas.insertar(nuevo_artista)

# Ventana principal
ventana_login = tk.Tk()
ventana_login.title("IPCArt-Studio")
ventana_login.geometry("800x600")

label_usuario = tk.Label(ventana_login, text="Usuario:")
label_contrasena = tk.Label(ventana_login, text="Contraseña:")
label_error = tk.Label(ventana_login, text="", fg="red")

entry_usuario = tk.Entry(ventana_login)
entry_contrasena = tk.Entry(ventana_login, show="*")

boton_login = tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_login, width=20, height=2, bg="orange")

label_usuario.pack()
entry_usuario.pack()
label_contrasena.pack()
entry_contrasena.pack()
boton_login.pack()
label_error.pack()

ventana_login.mainloop()
