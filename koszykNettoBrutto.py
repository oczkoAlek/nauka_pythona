def suma_koszyka(koszyk):
    suma = 0
    for pozycja in koszyk:
        #print('{0}: {1} ilosc {2}'.format(pozycja['nazwa'], pozycja['cena'], pozycja['ilosc']))
        suma = suma + pozycja['cena'] * pozycja['ilosc']
        #print('Suma: ' + str(suma))

    if wartosc == 'netto':
        return 
