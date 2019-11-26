AlinaLava = {'name': 'Alina', 'surname': 'Lava', 'role': 'Daughter', 'age': 18}
print AlinaLava['name'], AlinaLava['surname']
# AlinaLava['age'] = AlinaLava['age'] * 2
AlinaLava['age'] += 2
print AlinaLava
AlinaLava['age'] -= 2
print AlinaLava
AlinaLava['age'] *= 2
print AlinaLava

DimaLava = {}
DimaLava['name'] = 'Dima'
DimaLava['surname'] = 'Lava'
DimaLava['role'] = 'Brother'
DimaLava['age'] = 30
print DimaLava

keys = ['name', 'surname', 'role', 'age']
values = ['Nina', 'Lava', 'Mother', 54]
print zip(keys, values)
print list(zip(keys, values))
NinaLava = dict(zip(keys, values))
print NinaLava
"""
keys = ['name', 'surname', 'role', 'age']
values = ['Nina', 'Lava', 'Mother', 54]
morevalues = ['v1', 'v2', 'v3', 'v4']
print zip(keys, values, morevalues)
print list(zip(keys, values, morevalues))
# NinaLava = dict(zip(keys, values, morevalues)) - ValueError
print NinaLava

NinaLava.clear()
NinaLava = NinaLava.fromkeys(keys, 'Dont know')
print NinaLava
"""
family = [AlinaLava, DimaLava, NinaLava]
print family

for person in family:
    if person['age'] > 30:
        print person['name']

names = [person['name'] for person in family]
print names

totalage = sum(person['age'] for person in family)
print totalage

print [person['name'] for person in family if person['age'] > 36]

print [(person['age'] * 5 if person['role'] == 'Daughter' else person['name']) for person in family]
print [person['name'] for person in family if person['age'] == 30]