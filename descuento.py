def descuento(precio, porcentaje_descuento=10):
    precio_final = precio - (precio * porcentaje_descuento / 100)
    return precio_final

precio = float(input("Ingrese el precio del producto: "))
porcentaje = input("Ingrese el porcentaje de descuento (presione Enter para 10%): ")
if porcentaje == "":
    porcentaje = 10
else:
    porcentaje = float(porcentaje)
precio_con_descuento = descuento(precio, porcentaje)

print(f"El precio final después del descuento es: {precio_con_descuento}")
