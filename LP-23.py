Laevi = ['Nina', 'Tolya', 'Dima', 'Alina']
Member = ['Mother ', 'Father ', 'Brother ', 'Sister ']
family_members = []
index = 0
for man in Laevi:
    family_members.insert(index, Member[index] + Laevi[index])
    index = index + 1
print family_members
