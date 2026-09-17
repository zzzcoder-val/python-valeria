#inicio
print("Captura el total de la compra ")
compra = float(input())

#proceso 
iva = compra * 0.21
subtotal = iva + compra 

envío = subtotal * 0.05

total = envío + subtotal 

#salida
print(f"total a pagar: {total:,.2f} euros")