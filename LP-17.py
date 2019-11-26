"""
computers = 345
laptops = "lenovo"

if computers >= 300 and laptops == "lenovo":
    print 'Buy'

if computers >= 390 and laptops == "lenovo":
    print 'Buy'

if computers >= 390 or laptops == "lenovo":
    print 'Buy.'

pens = 45
pencils = 56
condition = pencils > pens
if condition:
    print 'yes'

pens = 90
pencils = 56
condition = pencils > pens
if not condition:
    print 'no'
"""
s = "DgkIFKLD"
print s.isalpha()

s = "DgkI FKLD"
print s.isalpha()

f = "G567FG89VBb"
print f.isalnum()

g = "234567"
print g.isdigit()

print f.islower()
print f.isupper()
print f.istitle()
print s.isspace()

name = raw_input("Hello! This is a string validator.What's your name?: ")
a = raw_input(name + ", type some symbols and hit Enter please: ")
if a.isdigit():
    print "You entered only digits."
else:
    print "You entered one or more non-digits or not only digits."
