from data.db_connection import db_connect as con


# CREATE
# READ

@con.connection_handler
def get_all_genres(cursor):
    sql_str = """
    SELECT * FROM genres
    """
    cursor.execute(sql_str)
    return cursor.fetchall()


@con.connection_handler
def get_shows_by_genre_id(cursor, genre_id):
    sql_str = """
    SELECT s.title, 
          to_char(s.rating, '9999.99') as rating,
          date_part('year', s.year) AS year
    FROM shows s
    JOIN show_genres sg on s.id = sg.show_id
    JOIN genres g on sg.genre_id = g.id
    WHERE g.id = %(genre_id)s
    """
    cursor.execute(sql_str, {'genre_id': genre_id})
    shows = cursor.fetchall()
    return shows

# UPDATE
# DELETE
