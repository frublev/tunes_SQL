import sqlalchemy
from create_tables import sql_create
from tunes import tunes_catalog, tunes_collection

tunes_db = 'postgresql://tunes_user:143180@localhost:5432/tunes'
engine = sqlalchemy.create_engine(tunes_db)
connection = engine.connect()


def create_tables(connect, request):
    connect.execute(request)
    return True


def delete_all_tables():
    request = '''
    SELECT table_name FROM information_schema.tables
    WHERE table_schema NOT IN ('information_schema','pg_catalog');'''
    tables = connection.execute(request).fetchall()
    print(tables)
    for table in tables:
        request = f'''drop table {table[0]} cascade;'''
        connection.execute(request)
    return True


def insert_data(data, table):
    request_1 = None
    request_2 = None
    album_in_db = None
    id_count = connection.execute(f'''SELECT max(id) from {table};''').fetchone()
    id_count = id_count[0]
    if id_count is None:
        id_count = 0
    id_count = id_count + 1
    for item in data:
        added_value1 = item[table]
        if table == 'genre' or table == 'singer':
            request_ = f'''
            INSERT INTO {table} 
            VALUES({id_count}, '{added_value1}');'''
        elif table == 'album' or table == 'collection':
            singer_id, album_id = None, None
            if table == 'album':
                request_albums = f'''
                SELECT id from {table}
                WHERE name = '{item[table]}';'''
                albums_id = connection.execute(request_albums).fetchall()
                if albums_id:
                    singers_list = []
                    singer_id_album = []
                    for album_id in albums_id:
                        request_singer_album = f'''
                        SELECT singer_id from singeralbum
                        WHERE album_id = {album_id[0]};'''
                        singer_id = connection.execute(request_singer_album).fetchone()
                        request_singer = f'''
                        SELECT name from singer
                        WHERE id = {singer_id[0]};'''
                        singer = connection.execute(request_singer).fetchone()
                        if singer[0] is not None:
                            singers_list.append(singer[0])
                            singer_id_album.append({'singer_id': singer_id[0], 'album_id': album_id})
                    if item['singer'] in singers_list:
                        album_in_db = True
                    else:
                        stop = len(singers_list) - 1
                        while stop > -1:
                            q = input(f'''Альбом {item['album']} записан: {singers_list[stop]}.
                            Это совместный альбом c {item['singer']}? (y/n):''')
                            if q == 'y':
                                stop = -1
                                album_in_db = True
                                request_singer = f'''
                                SELECT id from singer
                                WHERE name = '{item['singer']}';'''
                                singer_id = connection.execute(request_singer).fetchone()
                                singer_id = singer_id[0]
                                album_id = singer_id_album[stop]['album_id']
                                request_insert = f'''
                                INSERT INTO singeralbum 
                                VALUES({singer_id}, {album_id[0]});'''
                                connection.execute(request_insert)
                            elif q == 'n':
                                album_in_db = False
                                stop -= 1
                else:
                    album_in_db = False
                    singer_id_request = f'''
                    SELECT id from singer
                    WHERE name = '{item['singer']}';'''
                    singer_id = connection.execute(singer_id_request).fetchone()
                    singer_id = singer_id[0]
            if album_in_db:
                request_1 = None
            else:
                added_value2 = str(item['year']) + '-' + '01' + '-' + '01'
                request_1 = f'''
                INSERT INTO {table} 
                VALUES({id_count}, '{added_value1}', '{added_value2}');'''
                if table == 'album':
                    request_2 = f'''INSERT INTO singeralbum VALUES({singer_id}, {id_count});'''
        elif table == 'track':
            added_value2 = item['time']
            album_name = item['album']
            request_album_id = f'''
            SELECT id from album 
            WHERE name = '{album_name}';'''
            album_id_ = connection.execute(request_album_id).fetchone()
            added_value3 = album_id_[0]
            request_ = f'''
            INSERT INTO {table} 
            VALUES({id_count}, '{added_value1}','{added_value2}','{added_value3}');'''
        if request_1:
            try:
                connection.execute(request_1)
            except sqlalchemy.exc.IntegrityError:
                print('Нарушение уникальности ', added_value1)
            else:
                id_count += 1
        if request_2:
            connection.execute(request_1)
    check = f'''SELECT * from {table}'''
    return connection.execute(check).fetchall()


def match_tables(data, tables):
    s_request, _id = None, None
    table_name = tables[0]+tables[1]
    for tune in data:
        id_ = []
        for table in tables:
            if table == 'track':
                _id = []
                for track in tune['tracks']:
                    s_request0 = f'''
                    SELECT id from album 
                    WHERE name = '{track[1]}';'''
                    id_album = connection.execute(s_request0).fetchone()
                    id_album = id_album[0]
                    s_request1 = f'''
                    SELECT id, id_album from {table} 
                    WHERE name = '{track[0]}' AND id_album = {id_album};'''
                    id_track = connection.execute(s_request1).fetchone()
                    _id.append(id_track[0])
            else:
                s_request = f'''
                SELECT id from {table} 
                WHERE name = '{tune[table]}';'''
                _id = connection.execute(s_request).fetchone()
                _id = _id[0]
                print(tune['collection'])
            id_.append(_id)
        print(id_)
    #     i_request = f'''
    #     INSERT INTO {table_name}
    #     VALUES({id_[0]},{id_[1]});'''
    #     try:
    #         connection.execute(i_request)
    #     except sqlalchemy.exc.IntegrityError:
    #         print('Нарушение уникальности ', tune['track'])
    # check = f'''SELECT * from singergenre'''
    # print(connection.execute(check).fetchall())
    return True


order_match = [['singer', 'genre'], ['track', 'collection']]


if __name__ == "__main__":
    # delete_all_tables()
    # create_tables(connection, sql_create)
    # for o in order:
    #     print(insert_data(tunes_catalog, o))
    # print(insert_data(tunes_catalog, 'track'))
    match_tables(tunes_collection, ['track', 'collection'])
    # print(insert_data(tunes_collection, 'collection'))

# a = match_tables(pare)
# print(a)

# print(insert_data(tunes_catalog, 'singer'))

# aa = '''DELETE FROM singer;'''
# connection.execute(aa)


# table = 'Genre'
# g = 'swing1'
# a = f'''INSERT INTO {table} VALUES('{g}');'''
# connection.execute(a)

# a = '''INSERT INTO singer VALUES(1, 'The Dead South');'''


# b = '''SELECT * from singer'''
# c = connection.execute(b).fetchall()
# print(c)
