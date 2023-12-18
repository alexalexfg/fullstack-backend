"""Función para guardar los pedidos en el archivo txt"""
#nombre: "nombre"
#apellidos: "apellidos"

def guardar_pedido (nombre, apellido):
    """Función para guardar los pedidos en el archivo txt"""
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(-nombre + " " + apellido + "\n")
        file.close()

guardar_pedido("-Gabriel","García")
