import os

from estructuras.cola.nodo import Nodo


class Cola:
    def __init__(self):
        self.primero = None
        self.tamanio = 0

    def __len__(self):
        return self.tamanio
    
    #METODOS DE COLA
    #1. ENQUEUE: INSERTAR UN VALOR A LA COLA
    def enqueue(self, valor):
        #1. creamos un nuevo nodo
        nuevo = Nodo(valor)
        #2. si la cola esta vacia, el nuevo nodo es el primero
        if self.primero == None:
            self.primero = nuevo
        else:
            #3. si la cola no esta vacia, el nuevo nodo se coloca al final de la cola
            actual = self.primero
            while actual != None:
                #si el siguiente del nodo es nulo, ahi se inserta
                if actual.siguiente == None:
                    actual.siguiente = nuevo
                    break
                actual = actual.siguiente
        self.tamanio+=1
    
    #2. DEQUEUE: ELIMINA EL PRIMERO DE LA COLA
    def dequeue(self):
        #si la cola esta vacia, no se puede eliminar nada
        if self.primero == None:
            return None
        
        #si la cola tiene uno o más elementos
        #guardamos el valor que se va a eliminar
        valor_eliminado = self.primero.valor
        #actualizamos el primer nodo
        self.primero = self.primero.siguiente
        #actualizamos el tamaño
        self.tamanio-=1
        #retornamos el valor eliminado
        return valor_eliminado

    #3. VERPRIMERO: RETORNA EL PRIMERO DE LA COLA
    def verPrimero(self):
        if self.primero == None:
            return None
        return self.primero.valor
    
    #4. ISEMPTY: VERIFICAMOS SI LA COLA ESTA VACIA
    def isEmpty(self):
        return self.primero == None
    
    #5. GRAFICAR
    def graficar(self):
        if self.isEmpty():  # Verifica si la cola está vacía
            print("La cola está vacía. Generando representación de cola vacía.")
            
            # Generar un gráfico para la cola vacía
            codigodot = '''digraph G {
        rankdir="RL";
        label="Cola Vacía";
        node[shape=box];
        nodo0[label="Cola Vacía"];
    }
    '''
            # Crear nuestro archivo dot
            ruta_dot = 'reportesdot/cola_vacia.dot'
            archivo = open(ruta_dot, 'w')
            archivo.write(codigodot)
            archivo.close()

            # Generamos la imagen
            ruta_imagen = 'reportes/cola_vacia.png'
            comando = 'dot -Tpng ' + ruta_dot + ' -o ' + ruta_imagen
            os.system(comando)

            # Abrimos la imagen
            ruta2 = os.path.abspath(ruta_imagen)
            os.startfile(ruta2)
            return  # Sal de la función si la cola está vacía
#________________________________________________________        
        codigodot = ''
        codigodot +='''digraph G {
    rankdir="RL";
    label="Cola";
    node[shape=box];
    '''
        contador = 0
        #creamos los nodos
        actual = self.primero
        while actual != None:
            codigodot += 'nodo'+str(contador)+'[label=\"'+str(actual.valor)+'\"];\n'
            contador += 1
            actual = actual.siguiente

        #creamos los enlaces
        contador = 0
        actual = self.primero
        while actual.siguiente != None:
            codigodot+='nodo'+str(contador)+' -> nodo'+str(contador+1)+';\n'
            contador+=1
            actual = actual.siguiente
        
        codigodot+='}'

        #crear nuestro archivo dot
        ruta_dot = 'reportesdot/cola.dot'
        archivo = open(ruta_dot,'w')
        archivo.write(codigodot)
        archivo.close()

        #generamos la imagen
        ruta_imagen = 'reportes/cola.png'
        comando = 'dot -Tpng '+ruta_dot+' -o '+ruta_imagen
        os.system(comando)

        #abrimos la imagen
        ruta2 = os.path.abspath(ruta_imagen)
        os.startfile(ruta2)