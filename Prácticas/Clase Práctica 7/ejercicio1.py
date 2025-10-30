'''
Crear una clase llamada ListaCircularEnlazada que tenga almacenados datos tipo
entero y como atributos debe tener nodo cabeza y el tamanio de la lista actualizado.

La clase debe tener los siguientes metodos:

- agregar_al_final: agrega un nodo al final de la lista

- eliminar_nodo: eliminar un nodo especifico de la lista circular dado el valor contenido en ella

- mostrar_lista: muestra todos los elementos de la lista

- obtener_nodo_siguiente: metodo para obtener el nodo siguiente al nodo actual de la lista

'''

# Lista enlazada circular -> el ultimo nodo apunta al primero
# Nodo -> objeto que contiene un dato y la referencia al siguiente nodo

# head es una referencia al primer nodo de la lista -> o sea indica donde comienza la lista 
# acceso rapido al inicio -> desde head siempre puedo acceder rapidamente al primer elemento de la lista
# recorrido -> desde head puedo recorrer toda la lista siguiendo los enlaces (siguiente) de cada nodo hasta llegar
# al final

class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente=None
    def __str__(self):
        siguiente= self.siguiente.dato if self.siguiente else None
        return f"{self.dato} y mi siguiente es {siguiente}"
    

class ListaCircularEnlazada:
    
    # el dato de la lista es del tipo entero
    
    # Constructor
    def __init__(self, dato = 0):
        # queremos gestionar y actualizar la informacion internamente, por eso
        # head y size no los paso como parametros del constructor
        # cada vez que agrego o elimino un nodo usando los atributos de clase, estos atributos se 
        # actualizan automaticamente
        self.head = Nodo(dato) 
        self.head.siguiente = self.head 
        
        
        
        # En una lista circular, el último nodo siempre 
        # apunta de vuelta al head, y si la lista tiene un solo elemento, 
        # ese nodo apunta a sí mismo.
        # Por eso, en el constructor, cuando la lista tiene solo un nodo, 
        # se hace self.head.siguiente = self.head para mantener la estructura circular 
        # desde el principio.
        
        
    
        
        self.size = 1
        
        # Notar que self.head queda siempre con el primer nodo porque en los otros
        # metodos lo que hacemos es trabajar sobre otra variable: 'actual' que no modifica
        # nunca el valor de esta primera 
    
    def aplico_nodo(self, dato):
        if self.head is None:
            self.head = Nodo(dato)
        
        elif self.head.dato != dato:  # necesito que el dato al que estoy acediendo no exista todavia en la lista 
            nuevo_nodo =  Nodo(dato)
            nuevo_nodo.siguiente = self.head
            self.head = nuevo_nodo
        
        else:
            raise ValueError('El dato ya existe en la lista')

        self.size += 1

    def es_vacia(self):
        return self.size == 0 and self.head is None
    
    def agregar_al_final(self,dato):
        if not isinstance(self.head, Nodo):
            raise TypeError('El nodo debe ser de tipo Nodo')
        
        if not isinstance(dato, int):
            raise TypeError('El dato del nodo debe ser de tipo entero')

        actual = self.head 
        while actual.siguiente != self.head: # recorro hasta llegar al ultimo nodo
            actual = actual.siguiente
        
        # aca ya salio del bucle porque actual.siguiente es head (o sea llegue al ultimo nodo del ciclo circular)
        actual.siguiente = Nodo(dato) # el siguiente del ultimo nodo apunta al nuevo nodo 
        actual.siguiente.siguiente = self.head # el siguiente del nuevo nodo apunta al head 
        self.size += 1 # actualizo el tamanio de la lista 
    
    
    def eliminar_nodo(self,valor): 
        # lo que busco aca es que dado el dato pasado por parametro, elimine el nodo que contiene ese dato
        if self.es_vacia():
            raise ValueError('La lista esta vacia') 

        if not isinstance(valor,int):
            raise TypeError('El valor debe ser de tipo entero') 
        
        actual = self.head
        previo = None
        encontrado = False 
        while True:
            if actual.dato == valor:
                encontrado = True
                break 

            previo = actual # guardo el nodo previo
            actual = actual.siguiente

            if actual == self.head:  
                break                   # con esta condicion nos aseguramos de ponerle freno al bucle pues en una lista
                                        # circular el ultimo nodo enlaza devuelta con head, asi qu, si sigo avanzando con
                                        # actual = actual.siguiente, eventualmente volveremos al comienzo,
                                        # sin esa condicion, el while no tendria una condicion natural de parada y terminariamos
                                        # en un bucle infinito 

        if encontrado:
            if previo:
                previo.siguiente = actual.siguiente
            else:
                self.head = actual.siguiente

            self.size -= 1
        else:
            raise ValueError('El valor no se encuentra en la lista')
    
    def mostrar_lista(self):
        if self.es_vacia():
            print('La lista esta vacia')
        
        else:
            actual = self.head
            while actual:
                print(actual)
                actual = actual.siguiente
                if actual == self.head:
                    break
    
    
    def obtener_nodo_siguiente(self):
        # metodo para obtener el nodo siguiente al actual 
        actual = self.head
        if self.es_vacia():
            raise ValueError('La lista esta vacia')
        if actual.siguiente:
            return actual.siguiente

    # def __repr__(self):
    #     return f"ListaCircularEnlazada({self.head})"
    
    def __str__(self):
        if self.es_vacia():
            return "La lista esta vacia"
        
        else:
            actual = self.head
            nodos = []
            while actual:
                nodos.append(str(actual))    # esto llama al str de la clase nodo
                actual = actual.siguiente
                if actual == self.head:
                    break
            return " -> ".join(nodos)        # une todos los elementos de la lista con " -> " entre ellos

        
    def insertar_despues_de(self,valor_referencia: int, nuevo_dato: int):
        
        # Inserta un nuevo nodo inmediatamente despues del nodo
        # que contiene valor_referencia 
        
        
        # verifico si la lista esta vacia 
        if self.es_vacia():
            raise ValueError('La lista esta vacia')
        
        
        # verifico tipos de datos 
        if not isinstance(valor_referencia, int) or not isinstance(nuevo_dato: int):
            raise TypeError('Los valores deben ser enteros')
        
        # Empiezo el recorrido desde el nodo cabeza
        actual = self.head
        encontrado = False 
        
        # Como es una lista circular, usamos un bucle que corta cuando volvemos al inicio
        while True:
            # Si encuentro el nodo que tiene el valor de referencia 
            if actual.dato == valor_referencia:
                encontrado = True 
                
                # Creo el nuevo nodo 
                nuevo_nodo = Nodo(nuevo_dato)
                # El siguiete del nuevo nodo apunta al siguiente del actual
                nuevo_nodo.siguiente = actual.siguiente 
                # El siguiente del actual pasa a ser el nuevo nodo
                actual.siguiente = nuevo_nodo
                # Incremento el tamanio de la lista 
                self.size += 1 
                break
            
            # Avanzo al siguiente nodo
            actual = actual.siguiente 
            # Si vuelvo al head, significa que ya recorri toda la lista 
            if actual == self.head:
                break 
        
        # si termine el bucle sin encontrar el valor 
        if not encontrado:
            raise ValueError(f'El valor {valor_referencia} no se encuenra en la lista')

if __name__ == '__main__':
    lista = ListaCircularEnlazada(20)
    lista.agregar_al_final(10)
    lista.agregar_al_final(30)
    lista.agregar_al_final(40)
    
    print(lista)

    

