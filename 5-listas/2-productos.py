lista_productos = list()

for i in range(5):
    producto = input(f"Produto {i+1}:")
    lista_productos.append(producto)

lista_ordenada = sorted(lista_productos)

for producto in lista_ordenada:
    print(producto)

eliminar_producto = input("Que producto desea eliminar: ")
while not eliminar_producto in lista_ordenada:
    eliminar_producto = input("Ese producto no esta en la lista, ingrese otro: ")

lista_ordenada.remove(eliminar_producto)
print(f"{eliminar_producto} fue eliminado correctamente")

for producto in lista_ordenada:
    print(producto)