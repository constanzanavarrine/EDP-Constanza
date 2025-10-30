class Nodo():
    # constructor
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
    def __str__(self):
        # para devolver una cadena 
        siguiente = self.siguiente.dato if self.siguiente else None
        return f"[{self.dato} | {siguiente}]"