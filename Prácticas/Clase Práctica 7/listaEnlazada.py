class Nodo():
    def __init__(self, dato):
        self.dato = dato               # dato guardado en el nodo
        self.siguiente=None
    def __str__(self):
        siguiente= self.siguiente.dato if self.siguiente else None
        return f"{self.dato} y mi siguiente es {siguiente}"
    
# if __name__ == "__main__":
#     nodo1=Nodo(1)
#     nodo2=Nodo(2)
#     nodo3=Nodo(3)
#     print(nodo3)
#     nodo1.siguiente=nodo2
#     nodo2.siguiente=nodo3
#     # print(nodo1)
#     # print(nodo2)
#     # print(nodo3)
#     actual=nodo1
#     while actual:
#         print(actual.dato)
#         actual=actual.siguiente 
        
class ListaEnlazada():
    def __init__(self):
        self.inicio=None
    
    def esVacia(self):
        return self.inicio == None
    
    
    def agregarAlFinal(self,dato):
        nodo=Nodo(dato)

        if self.esVacia():
            self.inicio=nodo
        else:
            actual=self.inicio
            while actual.siguiente:
                actual=actual.siguiente
            actual.siguiente=nodo
            
    def agregarAlInicio(self,dato):
        nodo=Nodo(dato)
        if self.esVacia():
            self.inicio=nodo
        else:
            nodo.siguiente=self.inicio
            self.inicio=nodo
    
    def __str__(self):
        elementos=[]
        actual=self.inicio
        if actual==None:
            return "La lista esta vacia"
        else:
            while actual:
                elementos.append(str(actual.dato))
                actual=actual.siguiente
            return "->".join(elementos)
    
    def mostrar(self):
        if self.esVacia():
            print("La lista esta vacia")
        else:
            actual=self.inicio
            while actual:
                print(actual)
                actual=actual.siguiente
    
    def buscar_reemplazar(self,dato,nuevo): #busca el primer elemento que coincida y lo reemplaza
        if self.esVacia():
            print("La lista esta vacia")
        else:
            actual=self.inicio
            while actual:
                if actual.dato==dato:
                    actual.dato=nuevo
                    return True
                else:
                    actual=actual.siguiente
            return False
    
    def merge(self, otra_lista):
        '''
        Devuleve una nueva ListaEnlazada con los elementos intercalados
        L1E1, L2E2, L1E2, L2E2, .., y, si una lista es mas larga, agrega los sobrantes al final
        '''
    
        nueva = ListaEnlazada()
        a = self.inicio                 # self sera la lista que invoca el metodo
        b = otra_lista.inicio           # otra lista es la que se pasa por parametro 
        
        '''
        ya sabemos que el metodo merge solo se usa entre 
        objetos ListaEnlazada entonces inicio sera el puntero
        al primer nodo de la lista 
        
        .siguiente en cada nodo apunta al siguiente nodo o None
        si es el ultimo 
        '''
        while a is not None or b is not None:
            if a is not None:
                nueva.agregarAlFinal(a.dato)
                a = a.siguiente
            
            if b is not None:
                nueva.agregarAlFinal(b.dato)
                b = b.siguiente
        
        return nueva
    
    def a_lista(self):   # metodo para mostrar en formato lista
        out = []
        actual = self.inicio
        while actual:
            out.append(actual.dato)
            actual = actual.siguiente
        return out


if __name__ == "__main__":
    
    ####Recuerda por que crear el nodo No se debe crear afuera de la lista:
    #-Cada nodo debe pertenecer a una lista y no va tener dos veces el mismo nodo en una lista evitando errores(ciclo sin fin)
    #-Esto evita que un mismo nodo este en dos listas a la vez
    #-Evita que al cambiar el valor de un nodo en una lista, cambie en la otra
    #-Evita que al recorrer una lista, se recorra otra
      
    
    lista3=ListaEnlazada()
    lista2=ListaEnlazada()
    lista3.agregarAlFinal(2)
    lista3.mostrar()
    lista2.agregarAlFinal(2)
    lista2.mostrar()
    lista3.agregarAlFinal(12)
    lista3.mostrar()
    lista3.buscar_reemplazar(2,200)
    lista3.mostrar()
    
    l1 = ListaEnlazada()
    l2 = ListaEnlazada()

    # cargo datos
    for x in [1,2,3]:
        l1.agregarAlFinal(x)
    for x in [10,20,30]:
        l2.agregarAlFinal(x)

    # llamo al método merge
    resultado = l1.merge(l2)
    print(resultado.a_lista())

    
    
    
    
    
    

        
    
    