import random

class Cliente:
    def __init__(self, tiempo_llegada):
        self.tiempo_llegada = tiempo_llegada

class Pila:
    def __init__(self):
        self.pila = []

    def esta_vacia(self):
        return len(self.pila) == 0

    def apilar(self, elemento):
        self.pila.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.pila.pop()
        return None

    def ver_cima(self):
        if not self.esta_vacia():
            return self.pila[-1]
        return None

    def __len__(self):
        return len(self.pila)

def simular_cajero(tiempo_simulacion):
    cola = Pila()
    tiempo_actual = 0
    clientes_atendidos = 0
    primer_no_atendido = None

    while tiempo_actual < tiempo_simulacion:
        # Llega un nuevo cliente
        nuevo_cliente = Cliente(tiempo_actual)
        cola.apilar(nuevo_cliente)

        # Atención al cliente
        while not cola.esta_vacia() and tiempo_actual % (random.randint(2, 4) * 60) == 0:
            cliente_atendido = cola.desapilar()
            clientes_atendidos += 1

        # Actualizar tiempo
        tiempo_actual += random.randint(2, 3) * 60

        # Guardar el primer cliente no atendido
        if primer_no_atendido is None and not cola.esta_vacia():
            primer_no_atendido = cola.ver_cima().tiempo_llegada

    # Convertir el tiempo a horas y minutos
    horas = primer_no_atendido // 60
    minutos = primer_no_atendido % 60

    return clientes_atendidos, len(cola), f"{horas} horas y {minutos} minutos"

# Ejecutar la simulación
tiempo_simulacion = 10 * 60  # 10 horas en minutos
resultado = simular_cajero(tiempo_simulacion)

print("Clientes atendidos:", resultado[0])
print("Clientes en cola:", resultado[1])
print("Hora de llegada del primer cliente no atendido:", resultado[2])