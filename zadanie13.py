zwierzeta = {'name': 'Franek',
            'gatunek': 'kot',
            'kolor': 'czarny'}

print(zwierzeta['name'])
print(zwierzeta['gatunek'])

for k in zwierzeta:
    print("{0}:{1}".format(k, zwierzeta[k]))

for k, v in zwierzeta.items():
    print("{0}:{1}".format(k,v))
