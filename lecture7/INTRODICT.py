phonebook = {'Anirah': '777-1111', 'Mickey': '777-2222', 'Donald': '777-3333'}

print(phonebook)

print(phonebook['Mickey'])
print(phonebook.get('Donald'))

key = 'Pluto'
if key in phonebook:
    print(phonebook['pluto'])
else:
    print(key + 'Not in phonebook')

phonebook['Simson'] = '777-4567'
phonebook['pluto'] = '777-4444'
phonebook['mickey'] = '777-2122'
print(phonebook)

del phonebook['Simson']
print(phonebook)