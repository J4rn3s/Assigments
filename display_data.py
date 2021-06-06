line = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"

s = {}
(s['íd'], s['name'], s['country'], s['average'], s['board'], s['age']) = line.split(';')

print('ID:          ' + s['íd'])
print('Name:        ' + s['name'])
print('Country:     ' + s['country'])
print('Average:     ' + s['average'])
print('Board Type:  ' + s['board'])
print('Age:         ' + s['age'])