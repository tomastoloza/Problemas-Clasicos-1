# Problemas Clasicos de Programación Concurrente 1

# Productor Consumidor

## Ejercicio 1
````
Productor_Consumidor_1.py
````
El siguiente archivo python, contiene la definición de la clase ***listaFinita***, que extiende la clase list ([]) de modo que puede establecerse un limite máximo
    al tamaño (cantidad de objetos) de la lista.

A continuación implementa dos objetos derivados de Thread, un "Productor" que inserta elementos en la lista y un "Consumidor" que extrae elementos de la lista.
Finalmente instancia un conjuntos de threads Productor y Consumidor

"""
 
1. Leer y analizar que hace el código de este programa. 
**Analizar hasta comprender todas las líneas del código**

2. Ejecute el programa y analice los resultados. Con mucha probabilidad va a observar resultados inconsistentes y/o errores. Explique a que se deben.

3. **Utilizando Locks o RLocks solamente**, modificar los objetos Productor y Consumidor de modo que solucionen los erroes e inconsistencias.



## Ejercicio 2

1. **Sin alterar la clase *listaFinita***, modificar el programa de modo que el productor inserte objetos tupla de strings **tomados al azar** de la siguiente lista. 
```
[("España","Madrid"), ("Francia","Paris"),("Italia","Roma"),("Inglaterra","Londres"),("Alemania","Berlin",("Rusia","Moscu"),
("Turquia","Istambul"),("China","Pekin"), ("Japon","Tokio"),("Emiratos Arabes","Dubai"),("Argentina","Buenos Aires"),
("Brasil","Brasilia"),("Colombia","Bogota"),("Uruguay","Montevideo")]
```
Esta lista contiene tuplas ("pais", "capital"). 

El consumidor debe imprimir un mensaje: "La capital de "pais" es "capital".

El programa no debe mostrar inconsistencias ni errores debidos a condiciones de carrera o falta de sincronización.
