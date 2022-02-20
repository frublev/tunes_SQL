from itertools import combinations

tunes_catalog = [
    {'track': 'Banjo Odyssey',
     'singer': 'The Dead South',
     'album': 'Good Company',
     'year': 2014,
     'genre': 'bluegrass',
     'time': '00:05:09'},
    {'track': 'Beggin',
     'singer': 'Maneskin',
     'album': 'Chosen',
     'year': 2017,
     'genre': 'glam rock',
     'time': '00:03:29'},
    {'track': 'My love for Evermore',
     'singer': 'The Hillbilly Moon Explosion',
     'album': 'Buy, Beg or Steal',
     'year': 2011,
     'genre': 'rockabilly',
     'time': '00:03:24'},
    {'track': 'Bigger Life',
     'singer': 'The Cherry Poppin Daddies',
     'album': 'Bigger Life',
     'year': 2019,
     'genre': 'ska',
     'time': '00:03:48'},
    {'track': 'People Are Strange',
     'singer': 'The Doors',
     'album': 'Strange days',
     'year': 1967,
     'genre': 'psychedelia',
     'time': '00:03:05'},
    {'track': 'Star Of The County Down',
     'singer': 'Orthodox Celts',
     'album': 'The Celts Strike Again',
     'year': 1977,
     'genre': 'folk',
     'time': '00:02:25'},
    {'track': 'She s a Rainbow',
     'singer': 'The Rolling Stones',
     'album': 'Their Satanic Majesties Request',
     'year': 1967,
     'genre': 'psychedelia',
     'time': '00:02:25'},
    {'track': '(I Can t Get No) Satisfaction',
     'singer': 'The Rolling Stones',
     'album': 'Out of Our Heads',
     'year': 1965,
     'genre': 'hard rock',
     'time': '00:02:25'},
    {'track': 'Rose Tattoo',
     'singer': 'Dropkick Murphys',
     'album': 'Signed and Sealed in Blood',
     'year': 2013,
     'genre': 'folk',
     'time': '00:05:06'},
    {'track': 'Put A Lid On It',
     'singer': 'Squirrel Nut Zipppers',
     'album': 'Hot',
     'year': 1996,
     'genre': 'swing',
     'time': '00:02:39'},
    {'track': 'Pittin on the Ritz',
     'singer': 'The Cherry Poppin Daddies',
     'album': 'The Boop-a-Doo',
     'year': 2016,
     'genre': 'swing',
     'time': '00:03:39'},
    {'track': 'No surrender',
     'singer': 'The Meteors',
     'album': 'Wreckin Live',
     'year': 2002,
     'genre': 'psychobilly',
     'time': '00:03:16'},
    {'track': 'Immigrant Song',
     'singer': 'Led Zeppelin',
     'album': 'Led Zeppelin III',
     'year': 1970,
     'genre': 'hard rock',
     'time': '00:02:26'},
    {'track': 'Vicious',
     'singer': 'Halestorm',
     'album': 'Vicious',
     'year': 2018,
     'genre': 'hard rock',
     'time': '00:03:16'},
    {'track': 'West of Zanzibar',
     'singer': 'Squirrel Nut Zipppers',
     'album': 'Beasts of Burgundy',
     'year': 2018,
     'genre': 'swing',
     'time': '00:03:17'},
    {'track': 'Beasts of Burgundy',
     'singer': 'Squirrel Nut Zipppers',
     'album': 'Beasts of Burgundy',
     'year': 2018,
     'genre': 'swing',
     'time': '00:03:17'},
    {'track': 'Song One',
     'singer': 'Singer One',
     'album': 'Album One',
     'year': 2010,
     'genre': 'swing',
     'time': '00:03:17'},
    {'track': 'Song Two',
     'singer': 'Singer Two',
     'album': 'Album One',
     'year': 2010,
     'genre': 'swing',
     'time': '00:03:17'}
]


tunes_collection = [
    {'collection': 'bluegrass + glam rock + rockabilly',
     'tracks': [['Banjo Odyssey', 'Good Company'], ['Beggin', 'Chosen'], ['My love for Evermore', 'Buy, Beg or Steal']],
     'year': 2017},
    {'collection': 'bluegrass + glam rock + ska',
     'tracks': [['Banjo Odyssey', 'Good Company'], ['Beggin', 'Chosen'], ['Bigger Life', 'Bigger Life']],
     'year': 2019},
    {'collection': 'bluegrass + glam rock + psychedelia',
     'tracks': [['Banjo Odyssey', 'Good Company'], ['Beggin', 'Chosen'], ['People Are Strange', 'Strange days'],
                ['She s a Rainbow', 'Their Satanic Majesties Request']],
     'year': 2017},
    {'collection': 'bluegrass + glam rock + folk',
     'tracks': [['Banjo Odyssey', 'Good Company'], ['Beggin', 'Chosen'],
                ['Star Of The County Down', 'The Celts Strike Again'], ['Rose Tattoo', 'Signed and Sealed in Blood']],
     'year': 2017},
    {'collection': 'bluegrass + glam rock + hard rock',
     'tracks': [['Banjo Odyssey', 'Good Company'], ['Beggin', 'Chosen'],
                ['(I Can t Get No) Satisfaction', 'Out of Our Heads'], ['Immigrant Song', 'Led Zeppelin III'],
                ['Vicious', 'Vicious']],
     'year': 2018},
    {'collection': 'bluegrass + glam rock + swing',
     'tracks': [['Banjo Odyssey', 'Good Company'], ['Beggin', 'Chosen'], ['Put A Lid On It', 'Hot'],
                ['Pittin on the Ritz', 'The Boop-a-Doo'], ['West of Zanzibar', 'Beasts of Burgundy'],
                ['Beasts of Burgundy', 'Beasts of Burgundy'], ['Song One', 'Album One'], ['Song Two', 'Album One']],
     'year': 2018},
    {'collection': 'bluegrass + glam rock + psychobilly',
     'tracks': [['Banjo Odyssey', 'Good Company'], ['Beggin', 'Chosen'], ['No surrender', 'Wreckin Live']],
     'year': 2017},
    {'collection': 'bluegrass + rockabilly + ska',
     'tracks': [['Banjo Odyssey', 'Good Company'], ['My love for Evermore', 'Buy, Beg or Steal'],
                ['Bigger Life', 'Bigger Life']],
     'year': 2019}]


def collection_generate(tunes_, count_collections=1, genre_count=2):
    genre = []
    collections_list = []
    collections = None
    for tune in tunes_:
        collections = []
        if tune['genre'] not in genre:
            genre.append(tune['genre'])
        genre_list = list(combinations(genre, genre_count))
        for genre_ in genre_list:
            genre_ = list(genre_)
            collections.append(genre_)
    for count in range(count_collections):
        tunes_list = []
        year = 0
        for tune_ in tunes_:
            if tune_['genre'] in collections[count]:
                tunes_list.append([tune_['track'], tune_['album']])
                if tune_['year'] > year:
                    year = tune_['year']
        collection_name = ''
        for item in collections[count]:
            collection_name = collection_name + item + ' + '
        collection_name = collection_name[:-3]
        collections_list.append({'collection': collection_name, 'tracks': tunes_list, 'year': year})
    return collections_list


# print(collection_generate(tunes_catalog, 8, 3))
