import json

tracks = [{'name': 'Песня', 'artist': 'Агата Кристи'},
{'name': 'song', 'artist': 'Bob Marley'}]

with open('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(tracks, f)

print('Выполнено')

