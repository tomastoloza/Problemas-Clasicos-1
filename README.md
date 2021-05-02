# Problemas Clasicos de Programación Concurrente 1

## Productor Consumidor 1

````
Productor_Consumidor1.py
````

Clase listaFinita, extiende la clase list ([]) de modo que puede establecerse un limite máximo
    al tamaño (cantidad de objetos) de la lista.

    Uso:
    Declaración
    lista = listaFinita(Numero_Maximo_Items)
    # Crea una lista VACIA que admitirá hasta un máximo de Numero_Maximo_Items items

    El acceso a los elementos es igual que en una lista standard, la diferencia es que
    si se intenta agregar un elemento cuando la lista tiene Numero_Maximo_Items items, dara
    un mensaje de error y terminara el programa.

    Ejemplos
    Acceso al elemento i:

    a = lista[i]

    insertar un elemento en la posicón i.
    lista.insert(i, dato)  # si i es mayor que Numero_Maximo_Items termina el programa y da error

    o

    lista[i] = dato   # Si i es mayor que Numero_Maximo_Items termina el programa y da error.

    agregar un elemento al final de la lista

    lista.append(dato)  # Si la lista tiene Numero_Maximo_Items termina el programa y da error.

"""
