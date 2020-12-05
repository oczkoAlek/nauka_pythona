koszyk = [{'nazwa': 'orzechy', 'cena': 10},
        {'nazwa': 'olej', 'cena': 50},
        {'nazwa': 'maslo', 'cena': 100},
        {'nazwa': 'pomarancze', 'cena': 50}]
suma = 0
for pozycja in koszyk:
    print('{0}: {1}'.format(pozycja['nazwa'], pozycja['cena']))
    suma = suma + pozycja['cena']
print('Suma: ' + str(suma))
