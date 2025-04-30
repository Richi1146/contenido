# Diccionarios en Python 🐍

## ¿Qué es un diccionario?
Un **diccionario** es una estructura de datos en Python que almacena pares clave-valor. Las claves deben ser únicas e inmutables (como strings o números), y los valores pueden ser de cualquier tipo.

---

## 📌 Crear un diccionario

```python
# Diccionario vacío
mi_diccionario = {}

# Diccionario con datos
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá"
}
```
🔍 Acceder a valores
```python
print(persona["nombre"])     # Ana
print(persona.get("edad"))   # 25
print(persona.get("correo", "No existe"))  # Valor por defecto si no existe
```
✍️ Modificar valores
```python
persona["edad"] = 26
persona["profesion"] = "Ingeniera"  # Agrega nueva clave
```

# ❌ Eliminar elementos
```python
del persona["ciudad"]
persona.pop("edad")
persona.clear()  # Elimina todos los elementos
```
# 🔁 Recorrer un diccionario

# Solo claves
```python
for clave in persona:
    print(clave)
```
# Claves y valores
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
# Solo valores
```python
for valor in persona.values():
    print(valor)
```
# ✅ Otras funciones útiles  

# Obtener solo claves
```python
print(persona.keys())
```
# Obtener solo valores
```python
print(persona.values())
```
# Obtener pares clave-valor
```python
print(persona.items())
```
# Verificar si una clave existe
```python
if "nombre" in persona:
    print("Existe la clave 'nombre'")
```
🧪 Ejemplo completo
```python
usuario = {
    "username": "milecoder",
    "email": "mile@example.com",
    "activo": True
}

for clave, valor in usuario.items():
    print(f"{clave} => {valor}")
```
# 🧾 Listas de Diccionarios en Python

Una **lista de diccionarios** es una colección de diccionarios almacenados en una lista. Es útil para representar datos estructurados como registros de una base de datos, usuarios, productos, etc.


## 🛠️ Cómo crear una lista de diccionarios

```python
usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Sofía", "edad": 22}
]
```
# Cada elemento de la lista es un diccionario independiente.

🔁 Cómo recorrer una lista de diccionarios
```python
for usuario in usuarios:
    print(usuario["nombre"], "tiene", usuario["edad"], "años")
```
Puedes acceder a cada campo con su clave, como si fuera un registro.

# ✏️ Cómo modificar un diccionario dentro de la lista
```python
usuarios[0]["edad"] = 26  # Modificar el primer usuario
usuarios[1]["profesion"] = "Ingeniero"  # Agregar nueva clave a segundo
```
# ➕ Cómo agregar un nuevo diccionario a la lista
```python
nuevo_usuario = {"nombre": "Carlos", "edad": 28}
usuarios.append(nuevo_usuario)
```
También puedes usar insert() para agregarlo en una posición específica:
```python
usuarios.insert(1, {"nombre": "Lucía", "edad": 24})
```
# ❌ Cómo eliminar diccionarios de la lista
```python
usuarios.pop(2)  # Eliminar el tercer elemento
del usuarios[0]  # Eliminar el primero
```
🔍 Buscar dentro de la lista
```python
for usuario in usuarios:
    if usuario["nombre"] == "Ana":
        print("Usuario encontrado:", usuario)
```
🧠 Ejemplo completo
```python
productos = [
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Teclado", "precio": 45}
]
```
# Mostrar todos los productos
```python
for p in productos:
    print(f"{p['nombre']} cuesta ${p['precio']}")
```
# Aumentar el precio de todos en 10%
```python
for p in productos:
    p["precio"] *= 1.10
```
# Mostrar el nuevo listado
```python
print("\nPrecios actualizados:")
for p in productos:
    print(f"{p['nombre']} ahora cuesta ${p['precio']:.2f}")

```
