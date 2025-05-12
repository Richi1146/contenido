# Simulacro de Examen: Gestión de Inventario de una Librería en Python
# Caso de Uso (Épica):
# Como gerente de una librería, quiero un sistema que me permita gestionar el inventario de libros de manera eficiente, para que pueda realizar un seguimiento preciso de los títulos disponibles, su cantidad y los precios actualizados. Además, quiero poder calcular el valor total del inventario para saber cuánto dinero está invertido en los productos.

# Funcionalidades Principales:
# Para alcanzar un resultado óptimo en esta prueba, deberás implementar las siguientes funcionalidades en Python:

# 1. Añadir libros al inventario:
# Permitir al usuario agregar libros con atributos como: título, precio y cantidad disponible.
# Validar que el precio y la cantidad sean números positivos.
# 2. Consultar libros en inventario:
# Buscar un libro por su título y mostrar sus detalles (título, precio, cantidad).
# Si el libro no existe, mostrar un mensaje de error indicando que el libro no se encuentra en el inventario.
# 3. Actualizar precios de libros:
# Modificar el precio de un libro específico en el inventario.
# Validar que el nuevo precio sea un número positivo antes de realizar el cambio.
# 4. Eliminar libros del inventario:
# Permitir la eliminación de un libro que ya no está disponible.
# Confirmar la existencia del libro antes de eliminarlo.
# 5. Calcular el valor total del inventario:
# Calcular el valor total del inventario multiplicando el precio por la cantidad de cada libro.
# Mostrar el total acumulado con dos decimales.
# Criterios de Aceptación:
# El programa debe permitir agregar al menos 5 libros iniciales.
# Al consultar un libro, debe indicar si no existe en el inventario con un mensaje claro.
# La actualización de precios debe validar que el nuevo precio sea un número positivo.
# La eliminación de un libro debe confirmar su existencia antes de borrarlo.
# El cálculo del valor total del inventario debe ser preciso y mostrar el resultado con dos decimales.
# El código debe estar estructurado en funciones para cada operación.
# El código y los comentarios deben estar 100% en inglés (sin excepción alguna).
# Instrucciones:
# Crea una lista de libros iniciales con al menos 5 libros, donde cada libro sea un diccionario con las claves: title, price, y quantity.
# Implementa funciones para cada una de las funcionalidades mencionadas.
# La estructura general debe incluir un menú interactivo que permita a los usuarios seleccionar las acciones a realizar.
# Al finalizar, asegúrate de mostrar el valor total del inventario con dos decimales.
# Ejemplo de Libros Iniciales:
import re
inventory = [
    {"title": "Book 1", "price": 10.0, "quantity": 100},
    {"title": "Book 2", "price": 15.0, "quantity": 50},
    {"title": "Book 3", "price": 20.0, "quantity": 30},
    {"title": "Book 4", "price": 25.0, "quantity": 10},
    {"title": "Book 5", "price": 30.0, "quantity": 5}
]

def validate_simbols(message):
        woth = input(message).lower()
        if re.match(r"^[a-z0-9\s]+$", woth):  # Valida letras minusculas, numeros y espacios
            return woth
        else:
            print("Invalid entry, please try again.")
            return validate_simbols(message)  
    

def positive_number(text):
    while True:
        try:
            value = float(input(text))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def number_int(text):
    while True:
        try:
            value = int(input(text))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_product():
    product_name = validate_simbols("Product name: ")
    price = positive_number("Price: $")
    quantity = number_int("Available quantity: ")
    product = {"title": product_name, "price": price, "quantity": quantity}
    inventory.append(product)
    print(f"\nProduct added: {product_name}, Price: {price}, Quantity: {quantity}")

def consult_product():
    product_name = validate_simbols("Enter the name of the product to consult: ")
    for product in inventory:
        if product["title"].lower() == product_name.lower():
            print(f"\nProduct found: {product['title']}, Price: {product['price']}, Quantity: {product['quantity']}")
            return
    print("Product not found.")

def update_price():
    product_name = validate_simbols("Enter the name of the product to update: ")
    for product in inventory:
        if product["title"].lower() == product_name.lower():
            new_price = positive_number("New price: $")
            product["price"] = new_price
            print(f"Price updated for {product_name}: {new_price}")
            return
    print("Product not found.")

def delete_product():
    product_name = validate_simbols("Enter the name of the product to delete: ")
    for product in inventory:
        if product["title"].lower() == product_name.lower():
            inventory.remove(product)
            print(f"Product {product_name} removed.")
            return
    print("Product not found.")

def calculate_total_inventory():
    total = 0
    for product in inventory:
        total += product["price"] * product["quantity"]
    print(f"Total inventory value: ${total:.2f}")
    return total

def menu():
    while True:
        print('\n')
        print("1. Add products")
        print("2. Consult products")
        print("3. Update prices")
        print("4. Delete products")
        print("5. Total inventory value")
        print("6. Leave")
        print('\n')
        option = input('Enter the option you want: ')
        
        if option == '1':
            add_product()
        elif option == '2':
            consult_product()
        elif option == '3':
            update_price()
        elif option == '4':
            delete_product()
        elif option == '5':
            calculate_total_inventory()
        elif option == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

menu()

