class Persona:
    def __init__(self, id, pwd, NombreCompleto, CorreoElectronico, NumeroTelefono):
        self.id = id
        self.pwd = pwd
        self.NombreCompleto = NombreCompleto
        self.CorreoElectronico = CorreoElectronico
        self.NumeroTelefono = NumeroTelefono

    # Métodos get
    def get_id(self):
        return self.id

    def get_pwd(self):
        return self.pwd

    def get_nombre_completo(self):
        return self.NombreCompleto

    def get_correo_electronico(self):
        return self.CorreoElectronico

    def get_numero_telefono(self):
        return self.NumeroTelefono

    # Métodos set
    def set_id(self, id):
        self.id = id

    def set_pwd(self, pwd):
        self.pwd = pwd

    def set_nombre_completo(self, NombreCompleto):
        self.NombreCompleto = NombreCompleto

    def set_correo_electronico(self, CorreoElectronico):
        self.CorreoElectronico = CorreoElectronico

    def set_numero_telefono(self, NumeroTelefono):
        self.NumeroTelefono = NumeroTelefono

    def informacionDetallada(self):
        print(f"|{"----Persona Asignada-----":^61}|")
        print(f"|" + "-" * 30 + "|" + "-" * 30 + "|")
        print(f"|{"id":<30}|{self.id:<30}|")
        print(f"|{"pwd":<30}|{self.pwd:<30}|")
        print(f"|{"Nombre Completo":<30}|{self.NombreCompleto:<30}|")
        print(f"|{"Correo Electronico":<30}|{self.CorreoElectronico:<30}|")
        print(f"|{"Numero de Telefono":<30}|{self.NumeroTelefono:<30}|")
        print(f"|" + "-" * 61 + "|")