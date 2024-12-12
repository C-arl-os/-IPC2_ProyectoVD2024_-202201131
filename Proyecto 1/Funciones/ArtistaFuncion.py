import xml.etree.ElementTree as ET
from tkinter import filedialog, messagebox

from ObjetosPersonas.Artista import Artista_usados
from ObjetosPersonas.Persona import Persona
from ListaSimple.ListaSimple import ListaSimple

class ArtistaFucnion:
    
    def __init__(self):
        self.Lista_Artista = ListaSimple()
        
    # Métodos get
    def get_lista_artista(self):
        return self.Lista_Artista

    def get_artista(self, id):
        return self.Lista_Artista.obtenerUsuario(id)
    
    def mostrar_artistas(self):
        # self.Lista_Artista.imprimirLista()
        self.Lista_Artista.graficar()
            
    def agregarArtistas(self):
        # Seleccionar archivo XML
        
        ruta = filedialog.askopenfilename(title="Cargar Archivo", filetypes=(('Text files', '*.xml'), ('All files','*.*')))

        # Parsear el XML
        tree = ET.parse(ruta)
        root = tree.getroot()

        if root.tag == 'Artistas':
            # Iterar sobre cada elemento <Artista>
            for Artista in root:
                id = Artista.attrib['id']
                password = Artista.attrib['pwd']
                NombreCompleto = ""
                NumeroTelefono = ""
                CorreoElectronico = ""
                Especialidades = ""
                NotasAdicionales = ""

                # Procesar los hijos de cada <Artista>
                for hijo in Artista:
                    if hijo.tag == 'NombreCompleto':
                        NombreCompleto = hijo.text
                    elif hijo.tag == 'CorreoElectronico':
                        CorreoElectronico = hijo.text
                    elif hijo.tag == 'NumeroTelefono':
                        NumeroTelefono = hijo.text
                    elif hijo.tag == 'Especialidades':
                        Especialidades = hijo.text
                    elif hijo.tag == 'NotasAdicionales':
                        NotasAdicionales = hijo.text

                # Crear un nuevo objeto Artista_usados y agregarlo a la lista
                nuevo = Artista_usados(id, password, NombreCompleto, CorreoElectronico, NumeroTelefono, Especialidades, NotasAdicionales)
                self.Lista_Artista.insertar(nuevo)
            # print(f"Artista añadido: {NombreCompleto}")
