print('******* Bienvenido al sistema de descuentos *******')

MONTO_COMPRA_DESC=1000
DESCUENTO_MIEMBRO_Y_COMPRA=0.10
DESCUENTO_MIEMBRO_O_COMPRA=0.05

monto_compra = float(input('Ingrese el monto total de su compra: '))
es_miembro = input('Es miembro de la tienda? (si/no): ').strip().lower()

if (monto_compra >= MONTO_COMPRA_DESC) and (es_miembro == 'si'):
    descuento = DESCUENTO_MIEMBRO_Y_COMPRA
    print('Felicidades, has obtenido un descuento del 10%')
elif (monto_compra >= MONTO_COMPRA_DESC) or (es_miembro == 'si'):
    descuento = DESCUENTO_MIEMBRO_O_COMPRA
    print('Felicidades, has obtenido un descuento del 5%')
else:
    descuento = 0.0
    print('No has obtenido ningún descuento')

descuento_total = monto_compra * descuento
monto_total = monto_compra - descuento_total

print(f'Monto de la compra es: ${monto_compra}')
if descuento > 0:
    print(f'Monto del descuento: ${descuento_total}')
    print(f'Monto final de la compra con descuento: ${monto_total}')