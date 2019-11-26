"""
import re
a = raw_input()
a = a.strip('0')
print a
result = re.match(r'(\d{1,10}\.\d{1,10}){2,11}', a)
print result
"""
workfile = open("Alinchello.txt", "w")
workfile.write("This is me.")
workfile.write("\n")
workfile.write("Welcome!")
workfile.close()
print "Done"
