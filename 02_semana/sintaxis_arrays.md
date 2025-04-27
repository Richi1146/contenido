## Arrays
Los arrays son un formato que nos permite guardar varios datos en memoria
aqui aprenderas manipularlos:

# Crear una lista (array)

Su sintaxis es usando corchetes y por dentro son deparados por ,
```python
mi_lista = [1, 2, 3, 4, 5]
```
# Acceder a elementos 

```python
mi_lista = [10, 20, 30, 40]
# Acceder a un elemento por índice (comienza desde 0)
print(mi_lista[0])  # 10
# Acceder al último elemento con índice negativo
print(mi_lista[-1])  # 40
```
# Slicing (Rebanado)

```python
mi_lista = [10, 20, 30, 40, 50]
# Obtener sublistas
print(mi_lista[1:4])  # [20, 30, 40] (Desde el índice 1 hasta el 3)
print(mi_lista[:3])  # [10, 20, 30] (Desde el inicio hasta el índice 2)
print(mi_lista[2:])  # [30, 40, 50] (Desde el índice 2 hasta el final)
```

# Modificar elementos

```python
mi_lista = [10, 20, 30, 40]
# Cambiar un elemento por su índice
mi_lista[2] = 99  # [10, 20, 99, 40]
```

# Agregar elementos

```python
mi_lista = [10, 20, 30]
# Usar append() para agregar al final
mi_lista.append(40)  # [10, 20, 30, 40]
# Usar insert() para agregar en una posición específica
mi_lista.insert(1, 15)  # [10, 15, 20, 30, 40]
# Usar extend() para agregar una lista a otra
mi_lista.extend([50, 60])  # [10, 15, 20, 30, 40, 50, 60]
```

# Eliminar elementos

```python
mi_lista = [10, 20, 30, 40, 50]
# Usar remove() para eliminar un valor específico
mi_lista.remove(30)  # [10, 20, 40, 50]
# Usar pop() para eliminar y devolver el último valor
ultimo = mi_lista.pop()  # 50, y la lista queda [10, 20, 40]
# Usar pop() con índice para eliminar en una posición específica
mi_lista.pop(1)  # Elimina el elemento en la posición 1 (20), la lista queda [10, 40]
# Usar del para eliminar por índice o rango
del mi_lista[0]  # Elimina el primer elemento, lista queda [40]
```
# Buscar elementos

```python
mi_lista = [10, 20, 30, 40, 50]
# Usar in para verificar si un elemento está en la lista
print(20 in mi_lista)  # True
# Usar index() para obtener el índice de un elemento
print(mi_lista.index(30))  # 2
# Usar count() para contar cuántas veces aparece un elemento
print(mi_lista.count(20))  # 1
```

# Ordenar elementos

```python
mi_lista = [40, 10, 30, 20]
# Ordenar la lista en orden ascendente
mi_lista.sort()  # [10, 20, 30, 40]
# Ordenar en orden descendente
mi_lista.sort(reverse=True)  # [40, 30, 20, 10]
# Usar sorted() para devolver una lista ordenada sin modificar la original
lista_ordenada = sorted(mi_lista)  # [10, 20, 30, 40]
```

# Invertir una lista

```python
mi_lista = [10, 20, 30, 40]
# Usar reverse() para invertir la lista en su lugar
mi_lista.reverse()  # [40, 30, 20, 10]
# Usar slicing para invertir sin modificar la original
inverted_list = mi_lista[::-1]  # [10, 20, 30, 40]
```

# Copiar una lista

```python
mi_lista = [10, 20, 30]
# Usar slicing para hacer una copia
copia_lista = mi_lista[:]  # [10, 20, 30]
# Usar la función list() para hacer una copia
copia_lista = list(mi_lista)  # [10, 20, 30]
# Usar copy() para hacer una copia (en Python 3.3+)
copia_lista = mi_lista.copy()  # [10, 20, 30]
```

# Comprobar si la lista está vacía

```python
mi_lista = []
if not mi_lista:  # Si la lista está vacía
    print("La lista está vacía")
```


# como ingreso varios datos por consola a un array?

```python
# Crear una lista vacía
mi_lista = []

# Número de elementos a ingresar
n = int(input("¿Cuántos elementos quieres ingresar? "))

# Llenar la lista con los elementos
# Con el i + 1 mostramos el numero de producto en el que vamos, el orden, recuerda que empezamos desde 0 y por eso sumamos 1
# para que el usuario no vea 0 sino que empezamos desde 1
for i in range(n):
    elemento = input(f"Ingrese el elemento {i+1}: ")
    mi_lista.append(elemento)

# Mostrar la lista resultante
print("La lista es:", mi_lista)
```