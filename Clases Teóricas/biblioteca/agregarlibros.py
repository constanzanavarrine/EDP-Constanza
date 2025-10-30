from libro import Libro


    #crear libros
try:
    gabriel=Libro(' hola como estas1','Gabriel Garcia','Sudamericana','12345678')
    rayos=Libro('La Rayuela','Cortazar','Sudamericana','12345679')
    tunel=Libro('El tunel','Sabato','Bruguera','123456799')
    tunelsito=Libro('El tunel','Sabato','Bruguera','1234567991')


    print(gabriel)

    # armar diccionario para guardar los libros 
    diccionario_libros={
        gabriel.getter_ISBN():gabriel,   # o sea con getter obtengo isbn --> 12345678
        rayos.getter_ISBN:rayos,
        tunel.getter_ISBN():tunel
        
    }
    
    
    #visualizo el diccionario
    print(diccionario_libros)
    
   
    #visualizo las claves del diccionario
    print(diccionario_libros.keys())
    
    
    # visualizo los valores de las claves
    print(diccionario_libros.values())
    
   
    #visualizo cada libro del diccionario de libros
    for libro in diccionario_libros.values():
        print(libro)

   
    #agregar elemento al diccionario
    diccionario_libros[tunelsito.getter_ISBN()]=tunelsito
    
    
    #verifico la cantidad de libros
    print(len(diccionario_libros))

    tunelsito=Libro('El tunel','Hernesto Sabato','Bruguera','1234567991')
    
    
    #verifico que no permite claves repetidas
    
    diccionario_libros[tunelsito.getter_ISBN()]=tunelsito
    print(len(diccionario_libros))

    for libro in diccionario_libros.values():
        print(libro)

   
    # verificar si un isbn esta en mi diccionario de libros
    print('1234567991009' in diccionario_libros)
    
    print('19988292922 ' in diccionario_libros)
    print(diccionario_libros.get('1234567991','La clave no existe, agrega el objeto')) # el segundo parametro es el que mostramos si el objeto no existe 

    
    
    #eliminar objeto del diccionario # pop
    diccionario_libros.pop('1234567991') # recuerde que devuelve el libro eliminado
    print(diccionario_libros.pop('1234567991', 'El libro no existe')) # personalizo mensaje si no existe
                                                                        # devuelve el elemento que elimina 
    print(len(diccionario_libros))

   
   
    # setdefault, agrega el objeto si no existe el isbn
    libromagico=Libro('Harry Potter','JK Rowling','Ingles','1111111111' )
    
    diccionario_libros.setdefault(libromagico.getter_ISBN(),libromagico)
    print(len(diccionario_libros))

    diccionario_libros.setdefault(libromagico.getter_ISBN(),libromagico)   # como aca ya existe no lo crea nuevamente y tampoco genera error
                                                                            # → setdefault verifica existencia 
    print(len(diccionario_libros))
    
    diccionario_libros[libromagico.getter_estado]=libromagico               # en este caso se crea directamente 

    for libro in diccionario_libros.values():
        print(libro)
        
    
    
    # print(diccionario_libros['234567']) -> el codigo no se rompe por el exception del tipo KeyError
    
    
except ValueError as e:
    print('el erro es {e}')
    
except TypeError as e:
    print('el erro es {e}')

except KeyError:
    print('la clave no existe')
    
except  Exception as e:
    print(' soy el error {e}')