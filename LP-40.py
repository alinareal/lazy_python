def child(a, c, b=5):
    return a, b, c

print child(1, 34, 5)
print child(1, 34, 6)
print child(1, 34, b=6)
print child(a=1, c=34, b=6)
