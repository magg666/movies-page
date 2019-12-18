from data.db_connection import db_connect as con


# CREATE
# READ


@con.connection_handler
def get_shows(cursor, number, sort_by, order):
    sql_str = """
    SELECT s.id,
       title,
       date_part('year', year) AS year,
       runtime,
       CAST(rating AS float),
       string_agg(DISTINCT g.name, ' ')       AS genre_name,
       homepage,
       trailer
    FROM shows s
       LEFT JOIN show_genres sg on s.id = sg.show_id
       LEFT JOIN genres g on sg.genre_id = g.id
    GROUP BY s.id
    ORDER BY {0} {1} 
    LIMIT 15 OFFSET {2}
    
    """.format(sort_by, order, number)
    cursor.execute(sql_str, {'sort_by': sort_by,
                             'order': order,
                             'number': int(number)})
    all_shows = cursor.fetchall()
    return all_shows


@con.connection_handler
def get_one_show(cursor, show_id):
    sql_str = """
    SELECT s.id,
       s.title,
       date_part('year', year) AS year,
       s.runtime,
       s.trailer,
       s.homepage,
       s.rating,
       s.overview,
       string_agg(DISTINCT g.name, ', ') as genres
    FROM shows s
       LEFT JOIN show_genres sg on s.id = sg.show_id
       LEFT JOIN genres g on sg.genre_id = g.id
    WHERE s.id = %(show_id)s
    GROUP BY s.id
    """
    cursor.execute(sql_str, {'show_id': show_id})
    show_data = cursor.fetchone()
    return show_data


@con.connection_handler
def get_show_title_by_season(cursor, season_id):
    sql_str = """
    SELECT shows.title FROM shows
    JOIN seasons s on shows.id = s.show_id
    WHERE s.id = %(season_id)s
    """
    cursor.execute(sql_str, {'season_id': season_id})
    show_title = cursor.fetchone()
    return show_title


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
