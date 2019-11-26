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
print europe
print population

population['Kiev'] = 2804000
population['Warsaw'] = 1735000

print 'Moscow has the population of', population['Moscow'], 'people'
print 'Vilnus has the population of', population['Vilnus'], 'people'
print 'Vilnus has the population of', population[europe['Litva']], 'people'

print 'The capital of Belarus is', europe['Belarus'], '.'
print 'The capital of Latvia is', europe['Latvia'], '.'

for country, capital in europe.items():
    print 'The Capital Of %s Is %s' % (country, capital)

for capital, people in population.items():
    print 'The population of %s is %s' % (capital, people)

for country, capital in europe.items():
    print 'The %s has the capital of %s and the population here in it is %s' % (country, capital, population[europe[country]])


