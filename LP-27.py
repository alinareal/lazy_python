family = {'Mother': 'Nina', 'Father': 'Tolya', 'Brother': 'Dima'}
print family
"""
class = dict(mother='Nina', father='Tolya', brother='Dima')
print class

class = dict.fromkeys(['Alla', 'Vadim', 'Lena'])
print class
"""

voc = {key: 'man' for key in range(4)}
print voc

voc2 = {age: age + 4 for age in range(5)}
print voc2

voc3 = {age: age + age for age in range(5, 10)}
print voc3

family['Sister'] = 'Alina'
print family

pets = {'Cat': 'Murca', 'Dog': 'Roma'}
family.update(pets)
print family

