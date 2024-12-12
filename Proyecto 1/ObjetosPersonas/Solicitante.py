from .Persona import Persona

class Solicitante_usados(Persona):
    def __init__(self, id, pwd, NombreCompleto, CorreoElectronico, NumeroTelefono, Direccion):
        super().__init__(id, pwd, NombreCompleto, CorreoElectronico, NumeroTelefono)
        self.Direccion = Direccion

    # Métodos get
    def get_direccion(self):
        return self.Direccion

    # Métodos set
    def set_direccion(self, Direccion):
        self.Direccion = Direccion
        
    
    def informacionDetallada(self):
        super().informacionDetallada()
        print(f"|{'---Solicitante----':^61}|")
        print(f"|{'Direccion':<30}|{self.Direccion:<30}|")
        print(f"|" + "-" * 61 + "|")
        print("")
        
    def __str__(self):
        return (f"ID: {self.id}\\n" \
                f"Contraseña: {self.pwd}\\n" \
                f"Nombre Completo: {self.NombreCompleto}\\n" \
                f"Correo Electrónico: {self.CorreoElectronico}\\n" \
                f"Número de Teléfono: {self.NumeroTelefono}\\n" \
                f"Direccion: {self.Direccion}")
        