
# suma koszyka
def suma_koszyka(koszyk):
    suma = 0
    for pozycja in koszyk:
        #print('{0}: {1} ilosc {2}'.format(pozycja['nazwa'], pozycja['cena'], pozycja['ilosc']))
        suma = suma + pozycja['cena'] * pozycja['ilosc']
        #print('Suma: ' + str(suma))
    return suma

#rabat R1 5% dla koszyka z wiecej niz 3 rzeczy
def r1_5procent(koszyk, suma_poczatkowa):
    suma_po_rabacie = 0
    if len(koszyk) > 3 or suma_poczatkowa < 500:
        suma_po_rabacie = suma_poczatkowa - ((suma_poczatkowa * 5.0)/100)
    else:
        suma_po_rabacie = suma_poczatkowa
        #print('Suma po rabacie 5%: ' + str(suma_po_rabacie))
    return suma_po_rabacie

#rabat 10% znizki dla koszyka wiecej niz 500 pln
def r2_10procent(koszyk, suma_poczatkowa):
    suma_po_rabacie = 0
    if suma_poczatkowa > 500:
        suma_po_rabacie = suma_poczatkowa - ((suma * 10)/100)
        #print('Suma po rabacie 10%: ' + str(suma_po_rabacie))
    else:
        suma_po_rabacie = suma_poczatkowa
    return suma_po_rabacie

#znizka co 3 produkt gratis
def co_3_gratis(koszyk, suma_poczatkowa):
    suma_po_rabacie = 0
    i = 0
    #print(i)
    for pozycja in koszyk:
        i += 1
    #print(i)
    #print(pozycja)
        if i%3 == 0:
            #print('{0}: {1}'.format(pozycja['nazwa'], pozycja['cena']))
            suma_po_rabacie = suma_poczatkowa - pozycja['cena']
            #print('Suma po co 3 gratis: ' + str(suma_po_rabacie))
    return suma_po_rabacie

if __name__ == "__main__":
    koszyk = [{'nazwa': 'orzechy', 'ilosc': 2, 'cena': 100},
            {'nazwa': 'olej', 'ilosc': 3, 'cena': 500},
            {'nazwa': 'maslo', 'ilosc': 4, 'cena': 300},
            {'nazwa': 'pomarancze', 'ilosc': 5, 'cena': 50}]

    suma = suma_koszyka(koszyk)
    print('Suma przed rabatem: {0}'.format(suma))
    suma_po_rabacie = r1_5procent(koszyk, suma)
    print('Suma po rabacie 5%: {0}'.format(suma_po_rabacie))
    suma_po_rabacie2 = r2_10procent(koszyk, suma)
    print('Suma po rabacie 10%: {0}'.format(suma_po_rabacie2))
    suma_po_rabacie3 = co_3_gratis(koszyk, suma_po_rabacie2)
    print('Co trzeci produkt gratis, suma: {0}'.format(suma_po_rabacie3))




#znizka najtanszy produkt gratis
    def najtanszy(e):
        return e['cena']
    koszyk.sort(key=najtanszy)
#    suma_po_rabacie = suma_po_rabacie - koszyk[0]['cena']
#    print('Suma po odjeciu najtanszego: ' + str(suma_po_rabacie))
