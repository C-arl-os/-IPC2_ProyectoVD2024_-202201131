from .Persona import Persona
from lista_simple_circular.ListaCircular import ListaCircular

class Artista_usados(Persona):
    def __init__(self, id, pwd, NombreCompleto, CorreoElectronico, NumeroTelefono, Especialidades, NotasAdicionales):
        super().__init__(id, pwd, NombreCompleto, CorreoElectronico, NumeroTelefono)
        self.Especialidades = Especialidades
        self.NotasAdicionales = NotasAdicionales
        self.procesadas = ListaCircular()

    # Métodos get
    def get_especialidades(self):
        return self.Especialidades

    def get_notas_adicionales(self):
        return self.NotasAdicionales

    # Métodos set
    def set_especialidades(self, Especialidades):
        self.Especialidades = Especialidades

    def set_notas_adicionales(self, NotasAdicionales):
        self.NotasAdicionales = NotasAdicionales
        
    def informacionDetallada(self):
        super().informacionDetallada()
        print(f"|{'---Artista----':^61}|")
        print(f"|{'Especialidad':<30}|{self.Especialidades:<30}|")
        print(f"|{'Notas Adicionales':<30}|{self.NotasAdicionales:<30}|")
        print(f"|" + "-" * 61 + "|")
        print("")
    
    def __str__(self):
        return (f"ID: {self.id}\\n" \
                f"Contraseña: {self.pwd}\\n" \
                f"Nombre Completo: {self.NombreCompleto}\\n" \
                f"Correo Electrónico: {self.CorreoElectronico}\\n" \
                f"Número de Teléfono: {self.NumeroTelefono}\\n" \
                f"Especialidades: {self.Especialidades}\\n" \
                f"Notas Adicionales: {self.NotasAdicionales}")
        
    def insertarProcesadas(self, valor):
        self.procesadas.insertar(valor)