# Dado el siguiente carrito de compras:
#carrito_compras = {
#"manzanas": 2.5, 
#"bananas": 1.75, 
#"leche": 3.0, 
#"pan": 2.25, 
#"huevos": 2.0 }
#calcule el monto total a pagar.

carrito_compras = {
    "manzanas": 2.5, 
    "bananas": 1.75, 
    "leche": 3.0, 
    "pan": 2.25, 
    "huevos": 2.0
}
total = 0

for i in carrito_compras.values():
    total += i

print(f'El total de los productos es {total}')

#Otra forma:

total = 0

for i in carrito_compras.items():
    total += i[1]

print(f'El total de los productos es {total}')