# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input('Ingrese su peso en Kg: '))
alt = float(input('Ingrese su altura en mts: '))

imc = round((peso/alt)**2, 2) #Redondear a dos decimales

print(f'Tu índice de masa corporal es {imc}redondeado con dos decimales.')
