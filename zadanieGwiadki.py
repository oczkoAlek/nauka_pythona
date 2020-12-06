pobrane_haslo = 'secret'
print(len(pobrane_haslo))
dlugosc_haslo = len(pobrane_haslo)
nowe_haslo = ''
for i in pobrane_haslo:
    #print(i)
    index = pobrane_haslo.index(i)
    #print(index)
    if index == 0 or index == dlugosc_haslo - 1:
        #print(i)
        nowe_haslo = nowe_haslo + i
    else:
        #print('to jest dalej')
        i = "*"
        nowe_haslo = nowe_haslo + i
print(nowe_haslo)




for idx in range(len(pobrane_haslo)):
