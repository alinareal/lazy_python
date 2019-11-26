Laevi = ['Nina', 'Tolya', 'Dima', 'Alina']
Member = ['Mother ', 'Father ', 'Brother ']
family_members = []

for men in Member:
    for man in Laevi:
        family_members.append(men + man)
print family_members
