# 🧠 Estructuras Condicionales en Python
### 🔹 if
### ✅ ¿Para qué sirve?
Para tomar decisiones. Si una condición es verdadera, se ejecuta un bloque de código.

### 🕒 ¿Cuándo usarlo?
Cuando necesitas hacer algo solo si se cumple cierta condición.

 >🔍 Ejemplo:

```python
edad = int(input("¿Cuántos años tienes? "))
if edad >= 18:
    print("Eres mayor de edad")
```
Si el usuario escribe 20, se imprimirá "Eres mayor de edad". Si pone 17, no se imprimirá nada (porque no hay un else).

### 🔹 if + else
### ✅ ¿Para qué sirve?
Para decidir entre dos opciones: si se cumple una condición, se hace algo; si no, se hace otra cosa.

### 🕒 ¿Cuándo usarlo?
Cuando siempre debe ejecutarse una de dos posibles acciones.

> 🔍 Ejemplo:
```python
numero = int(input("Escribe un número: "))
if numero > 0:
    print("Es positivo")
else:
    print("Es negativo o cero")
```    
## 🔹 if + elif + else

### ✅ ¿Para qué sirve?
Para elegir entre varias opciones. Se prueban varias condiciones una tras otra.

### 🕒 ¿Cuándo usarlo?
Cuando tienes más de dos posibilidades.

> 🔍 Ejemplo:
```python
nota = float(input("Escribe tu nota: "))
if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprobado")
else:
    print("Reprobado")
```

## 🔹 match case
Python no tiene switch-case como otros lenguajes (como C, Java o JavaScript), pero desde Python 3.10 se puede usar una estructura parecida llamada match-case.

### ✅ ¿Para qué sirve?
Para comparar una variable contra varios posibles valores y ejecutar una acción distinta para cada uno.

### 🕒 ¿Cuándo usarlo?
Cuando una misma variable puede tener varios valores específicos, y quieres una opción distinta para cada valor.

🔍 Ejemplo con match-case (Python 3.10+):
```python
opcion = input("Elige una fruta (manzana, banana, naranja): ")

match opcion:
    case "manzana":
        print("Elegiste manzana 🍎")
    case "banana":
        print("Elegiste banana 🍌")
    case "naranja":
        print("Elegiste naranja 🍊")
    case _:
        print("Fruta no reconocida")
```        
📝 case _: funciona como el else en un if, y se ejecuta si ninguna opción anterior coincide.

# 🔁 Bucles en Python (repetición de acciones)

## 🔹 while
### ✅ ¿Para qué sirve?
Para repetir un bloque de código mientras una condición sea verdadera.

### 🕒 ¿Cuándo usarlo?
Cuando no sabes cuántas veces se repetirá la acción, pero quieres que siga hasta que algo cambie.

> 🔍 Ejemplo:
```python
contador = 1
while contador <= 5:
    print("Número:", contador)
    contador += 1
Imprime del 1 al 5. El bucle termina cuando contador llega a 6.
```

## 🔹 for

### ✅ ¿Para qué sirve?
Para recorrer una secuencia (como una lista, un string o un rango de números).

### 🕒 ¿Cuándo usarlo?
Cuando sí sabes cuántas veces quieres repetir algo o cuando estás recorriendo elementos(listas), en este caso un string.

> 🔍 Ejemplo:
```python
nombre = "Ana"
for letras in nombre:
    print("Hola", letras)
```
Imprime un saludo para cada letra en la lista.

## 🔸 Extra: range()
Te permite repetir un bucle for un número fijo de veces.
```python
for i in range(3):  # Va desde 0 hasta 2
    print("Iteración:", i)
```
### 🔸 Extra: break y continue

> break → Sale del bucle antes de terminar.
> continue → Salta una vuelta y sigue con la siguiente.
```python
for i in range(5):
    if i == 3:
        break  # se detiene al llegar a 3
    print(i)
```
## Resultado: 0, 1, 2