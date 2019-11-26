europe = {
    'Belarus': 'Minsk',
    'Russia': 'Moscow',
    'Litva': 'Vilnus',
    'Latvia': 'Riga'
}
population = {
    'Minsk': 1911000,
    'Moscow': 11920000,
    'Vilnus': 543060,
    'Riga': 640319
}
"""
population.clear()
print population
"""
people = population.copy()
print population
print people

print population.keys()
print population.values()

country1 = europe.get('Belarus')
country2 = europe['Belarus']
print country1, country2

country3 = europe.get('Litva')
if not country3:
    print 'Sorry, there are no info.'
if country3:
    print country3

animals = {'names': ['Bob', 'Marley', 'Frank'], 'species': ['Dog', 'Cat', 'Frog']}
print animals['names'][1]
print animals['species'][1]