NinaLava = {
    'alias': 'NinaLava',
    'name': {'first': 'Nina', 'last': 'Lava'},
    'role': 'Mother',
    'characteristics': {'weight': 101, 'height': 179}
}
print NinaLava['characteristics']
print NinaLava['characteristics']['height']
DimaLava = {
    'alias': 'DimaLava',
    'name': {'first': 'Dima', 'last': 'Lava'},
    'role': 'Son',
    'characteristics': {'weight': 80, 'height': 182}
}
AlinaLava = {
    'alias': 'AlinaLava',
    'name': {'first': 'Alina', 'last': 'Lava'},
    'role': 'Daughter',
    'characteristics': {'weight': 64, 'height': 169}
}
family = [NinaLava, DimaLava, AlinaLava]
print family

for person in family:
    person['characteristics']['weight'] += 21
print family

for person in family:
    if person['name']['first'] == 'Alina':
        person['characteristics']['height'] += 3
print family

europe = {
    'Belarus': 'Minsk',
    'Russia': 'Moscow',
    'Litva': 'Vilnus',
    'Latvia': 'Riga'
}
del europe['Russia']
print europe
del NinaLava['name']['first']
print NinaLava

for person in family:
    del person['characteristics']['height']
print family
