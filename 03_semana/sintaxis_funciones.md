# 🧠 ¿Qué es una función en Python?
Una función es un bloque de código reutilizable que se ejecuta cuando se le llama. Sirve para organizar tu programa, evitar repetir código y hacerlo más legible.

```python
def saludar():
    print("Hola, ¿cómo estás?")
```
Para ejecutar esta función, simplemente la llamas:
```python
saludar()
```

# 🧩 ¿Qué son los parámetros y los argumentos?
## ✅ Parámetros:
Son variables que defines entre paréntesis cuando creas una función. Actúan como entradas que la función puede usar.

```python
def saludar(nombre):  # 'nombre' es un parámetro
    print(f"Hola, {nombre}")
```
##  ✅ Argumentos:
Son los valores reales que le pasas a la función cuando la llamas.

```python
saludar("Mile")
```
# ✨ Función con múltiples parámetros

```python
def sumar(a, b):
    resultado = a + b
    return resultado

print(sumar(3, 5))  # 8
```
# 🧰 Tipos de argumentos

Python permite distintos tipos de argumentos:
1. Argumentos posicionales (orden importa)

```python
def resta(a, b):
    return a - b

print(resta(10, 3))  # 7
```
2. Argumentos con nombre (keyword arguments)

```python
print(resta(b=3, a=10))  # 7
```
3. Parámetros con valor por defecto

```python
def saludar(nombre="invitado"):
    print(f"Hola, {nombre}")

saludar()          # Hola, invitado
saludar("Lucía")   # Hola, Lucía
```

# 🔄 Return vs print
```python
print() → Muestra un resultado en pantalla.

return → Devuelve un valor para que pueda usarse después.
```
```python
def doble(x):
    return x * 2

resultado = doble(4)
print(resultado)  # 8

```
y con print:

```python
def doble(x):
    print x * 2

resultado = doble(4) # 8
print(resultado)  # none

```

# 🔹 1. Variables Globales
Se definen fuera de cualquier función.

Están disponibles en todo el programa.

```python
x = 10  # variable global

def mostrar():
    print(x)  # accede a la variable global
mostrar()  # 10
```
# 🔸 2. Variables Locales
Se definen dentro de una función.
Solo existen mientras se ejecuta la función.
No pueden usarse fuera de la función.

```python
def saludo():
    mensaje = "Hola"  # variable local
    print(mensaje)

saludo()        # Hola
# print(mensaje)  # ❌ Error: mensaje no está definida fuera de la función
```
# ⚠️ ¿Qué pasa si quiero usar una variable global dentro de una función y modificarla?
Tienes que usar la palabra clave global:

```python
contador = 0

def aumentar():
    global contador
    contador += 1

aumentar()
print(contador)  # 1
```

si solo quieres usar el valor lo pasas como argumento

```python
contador = 0

def aumentar(numero):
    numero += 10
    return numero

aumentar(contador)  # 10
print(contador)  # 0
```