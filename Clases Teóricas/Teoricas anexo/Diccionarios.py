from ClasePersona import Persona

# Primera forma de crear un diccionario 

ninfa = Persona('Ninfa', 5555555, 20, 'F')
dana = Persona('Dana',9111111,20,'F')
maria = Persona('Maria', 92372822, 20, 'F')
diccionario = {}
print(diccionario)

# Segunda forma de crear un diccionario 

diccionario1 = dict()
print(diccionario1)

# llenar diccionario primer forma de llenado 
diccionario['ninfa'] = ninfa
diccionario['pedro'] = dana
diccionario['maria'] = maria

print(diccionario)
print(diccionario['pedro'])


# Para cambiar datos, simplemente:

diccionario['dana'] = dana
print(diccionario['dana'])


# podemos ver la longitud de un diccionario
print(len(diccionario))


diccionario1 = {'total':55, 10: 'Estructura de Datos', 'a': 55}



# Verificar que una clave esta en un diccionario

if 'total' in diccionario1:
    print(True)
else:
    print(False)
    
    
print(11 in diccionario1)


# Llaves de un diccionario
print(diccionario1.keys())


# Valores en un diccionario 
print(diccionario1.values())


# Todos los items del diccionario
print(diccionario1.items())    # esto me devuelve una tupla 


# Como movernos en un diccionario 
for keys,values in diccionario1.items():
    print(keys,values)
    
    
    
# Diccionario que simula una agenda de contactos 
agenda_contactos = {
                    'Ninfa Delgado': 27819191,
                    'Constanza Navarrine': 2903033
}


# Diccionario con dict()
agrendar_contactos = dict('Ninfa'==8299222,'Constanza'==9283389)