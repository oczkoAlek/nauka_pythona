koszyk = [{'nazwa': 'orzechy', 'cena': 100},
        {'nazwa': 'olej', 'cena': 500},
        {'nazwa': 'maslo', 'cena': 300},
        {'nazwa': 'pomarancze', 'cena': 50}]
suma = 0
for pozycja in koszyk:
    print('{0}: {1}'.format(pozycja['nazwa'], pozycja['cena']))
    suma = suma + pozycja['cena']

print('Suma: ' + str(suma))
print(len(koszyk))

if len(koszyk) > 3 and suma < 500:
    suma_po_rabacie = suma - ((suma * 5)/100)
    print('Suma po rabacie 5%: ' + str(suma_po_rabacie))

if suma > 500:
    suma_po_rabacie = suma - ((suma * 10)/100)
    print('Suma po rabacie 10%: ' + str(suma_po_rabacie))

else:
    suma_po_rabacie = suma

def najtanszy(e):
    return e['cena']
#print(suma)
koszyk.sort(key=najtanszy)
suma_po_rabacie = suma_po_rabacie - koszyk[0]['cena']
print('Suma po odjeciu najtanszego: ' + str(suma_po_rabacie))
