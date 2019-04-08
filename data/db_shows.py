from db_connection import db_connect as con


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
