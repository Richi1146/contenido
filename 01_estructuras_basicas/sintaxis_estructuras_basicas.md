# 🐍 Introducción a Python desde Cero

Este documento es una guía sencilla y clara para entender la **sintaxis básica de Python**, **declaración de variables**, **tipos de datos** y **operadores lógicos**.

## 👋 Mostrar mensajes en consola

En Python usamos la función `print()` para mostrar mensajes al usuario.

### 📌 Ejemplo:

```python
print("¡Hola, mundo!")
print("Este es un mensaje en pantalla.")
```

## 🎤 Pedir datos al usuario

Para solicitar información por consola usamos la función input().
### 📌 Ejemplo:

```python
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)
```
> 🧠 **Recuerda:** `input()` siempre devuelve un dato tipo `str` (cadena).

## 🔗 Concatenación

Existen varias formas de unir texto (concatenar) en Python. Aquí te mostramos las dos más comunes:
1. Usando comas , (recomendado para principiantes)

nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)

  > ✅ Python agrega un espacio automáticamente entre los elementos.

  > ✅ Puedes imprimir diferentes tipos de datos sin convertirlos.

2. Usando el operador +
```python
nombre = input("¿Cómo te llamas? ")
print("Hola " + nombre)
```
  >  ✅ Une cadenas directamente.

  >  ⚠️ Todos los elementos deben ser tipo str.
```python
edad = input("¿Cuántos años tienes? ")
print("Tienes " + edad + " años.")
```
  >  **🔎 Nota:** Si intentas concatenar un número (por ejemplo int) usando +, debes convertirlo con str().
```python
edad = 18
print("Tienes " + str(edad) + " años.")
```

## 🧠 Tipos de datos en Python

| Tipo   | Ejemplo       | Descripción                 |
|--------|---------------|-----------------------------|
| `str`  | `"Hola"`      | Cadena de texto             |
| `int`  | `10`          | Número entero               |
| `float`| `3.14`        | Número decimal              |
| `bool` | `True`, `False` | Booleano: verdadero o falso |

## 🔍 Saber el tipo de dato

Puedes usar la función type() para saber qué tipo de dato tienes.
### 📌 Ejemplo:
```python
numero = 10
print(type(numero))  # <class 'int'>

nombre = "Ana"
print(type(nombre))  # <class 'str'>
```

## 🧮 Operadores Aritméticos

| Operador | Descripción       | Ejemplo   | Resultado |
|----------|-------------------|-----------|-----------|
| `+`      | Suma              | `4 + 2`   | `6`       |
| `-`      | Resta             | `5 - 3`   | `2`       |
| `*`      | Multiplicación    | `2 * 3`   | `6`       |
| `/`      | División          | `6 / 2`   | `3.0`     |
| `//`     | División entera   | `7 // 2`  | `3`       |
| `%`      | Módulo (residuo)  | `5 % 2`   | `1`       |
| `**`     | Potencia          | `2 ** 3`  | `8`       |

## 🧠 Jerarquía de Operadores Aritméticos

El orden en que Python resuelve operaciones es el siguiente:

    () Paréntesis

    ** Potencia

    *, /, //, % Multiplicación, división, división entera y módulo

    +, - Suma y resta

### 📌 Ejemplo:
```python
resultado = 3 + 2 * 5
# Primero se multiplica: 2 * 5 = 10
# Luego se suma: 3 + 10 = 13
print(resultado)
```
## 🔗 Operadores Lógicos

| Operador | Descripción        | Ejemplo           | Resultado |
|----------|--------------------|-------------------|-----------|
| `and`    | Devuelve `True` si ambos son `True` | `True and False`  | `False`   |
| `or`     | Devuelve `True` si al menos uno es `True` | `True or False`   | `True`    |
| `not`    | Invierte el valor lógico | `not True`        | `False`   |

## 🧪 Operadores de Comparación

| Operador | Descripción              | Ejemplo        | Resultado |
|----------|--------------------------|----------------|-----------|
| `==`     | Igual a                  | `5 == 5`       | `True`    |
| `!=`     | Distinto de              | `5 != 3`       | `True`    |
| `>`      | Mayor que                | `5 > 3`        | `True`    |
| `<`      | Menor que                | `2 < 1`        | `False`   |
| `>=`     | Mayor o igual que        | `3 >= 3`       | `True`    |
| `<=`     | Menor o igual que        | `4 <= 2`       | `False`   |


### 🎓 Ejemplo combinado
```python
# Pedimos el nombre al usuario (siempre se guarda como texto)
nombre = input("¿Cuál es tu nombre? ")

# Pedimos la edad y la convertimos a entero, ya que input() devuelve texto
edad = int(input("¿Cuántos años tienes? "))

# Verificamos si es mayor de edad (18 o más)
es_mayor = edad >= 18

# Mostramos los resultados
print("Hola,", nombre)
print("¿Eres mayor de edad?", es_mayor)
print("Tipo de dato de 'edad':", type(edad))

```




