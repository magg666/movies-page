from db_connection import db_connect as con


# CREATE
# READ


@con.connection_handler
def get_shows(cursor, number):
    sql_str = """
    SELECT s.id,
       title,
       date_part('year', year) AS year,
       runtime,
       CAST(rating AS float),
       array_agg(g.name)       AS genre_name
    FROM shows s
       LEFT JOIN show_genres sg on s.id = sg.show_id
       LEFT JOIN genres g on sg.genre_id = g.id
    GROUP BY s.id
    ORDER BY rating DESC 
    LIMIT 15 OFFSET '{0}'
    
    """.format(number)
    cursor.execute(sql_str, {'number': int(number)})
    all_shows = cursor.fetchall()
    return all_shows


@con.connection_handler
def count_series(cursor):
    sql_str = """
    SELECT count(title) as show_amount FROM shows    
    """
    cursor.execute(sql_str)
    show_amount = cursor.fetchone()
    return show_amount

# UPDATE
# DELETE
