
# suma koszyka
def suma_koszyka(koszyk):
    suma = 0
    for pozycja in koszyk:
        #print('{0}: {1} ilosc {2}'.format(pozycja['nazwa'], pozycja['cena'], pozycja['ilosc']))
        suma = suma + pozycja['cena'] * pozycja['ilosc']
        #print('Suma: ' + str(suma))
    return suma
#rabat R1 5% dla koszyka z wiecej niz 3 rzeczy
def r1_5procent(koszyk, suma):
        if len(koszyk) > 3 and suma < 500:
            suma_po_rabacie = suma - ((suma * 5)/100)
            print('Suma po rabacie 5%: ' + str(suma_po_rabacie))
        return suma_po_rabacie

if __name__ == "__main__":

    koszyk = [{'nazwa': 'orzechy', 'ilosc': 2, 'cena': 100},
            {'nazwa': 'olej', 'ilosc': 3, 'cena': 500},
            {'nazwa': 'maslo', 'ilosc': 4, 'cena': 300},
            {'nazwa': 'pomarancze', 'ilosc': 5, 'cena': 50}]

    suma = suma_koszyka(koszyk)
    print('Suma: ' + str(suma))
    suma = r1_5procent(koszyk, suma)
    print('Suma po rabacie 5%: ' + str(suma))


#rabat 10% znizki dla koszyka wiecej niz 500 pln
    if suma > 500:
        suma_po_rabacie = suma - ((suma * 10)/100)
        print('Suma po rabacie 10%: ' + str(suma_po_rabacie))
    else:
        suma_po_rabacie = suma

#znizka co 3 produkt gratis
    i = 0
#print(i)
    for pozycja in koszyk:
        i += 1
    #print(i)
    #print(pozycja)
        if i%3 == 0:
        #print('{0}: {1}'.format(pozycja['nazwa'], pozycja['cena']))
            suma_po_rabacie = suma_po_rabacie - pozycja['cena']
            print('Suma po co 3 gratis: ' + str(suma_po_rabacie))

#znizka najtanszy produkt gratis
    def najtanszy(e):
        return e['cena']
    koszyk.sort(key=najtanszy)
    suma_po_rabacie = suma_po_rabacie - koszyk[0]['cena']
    print('Suma po odjeciu najtanszego: ' + str(suma_po_rabacie))
