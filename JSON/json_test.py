import json

# WRITING INTO JSON
data = {}
data['people'] = []

data['people'].append({
    'name': 'Scott',
    'website' : 'stackabuse.com',
    'from' : 'Nebraska'
})

data['people'].append({
    'name': 'Larry',
    'website' : 'google.com',
    'from' : 'Michigen'
})

data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

print(data)

# READING FROM JSON
with open('data.txt') as json_file:
    data_read = json.load(json_file)
    for p in data_read['people']:
        print('Name: ' + p['name'])
        print('Web: ' + p['website'])
        print('From: ' + p['from'])
        print('')
