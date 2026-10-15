precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
subtotal = precio * cantidad
iva = subtotal * 0.16
total = subtotal + iva
print(f"Total: ${total:.2f}")