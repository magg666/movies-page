from db_connection import db_connect as con


# CREATE
# READ
@con.connection_handler
def get_all_actors_for_one_show(cursor, show_id):
    sql_str = """
    SELECT actors.id, name FROM actors
      LEFT JOIN show_characters sc on actors.id = sc.actor_id
      LEFT JOIN shows s on sc.show_id = s.id
    WHERE s.id = %(show_id)s
    GROUP BY actors.id
    """
    cursor.execute(sql_str, {'show_id': show_id})
    actors = cursor.fetchall()
    return actors


# UPDATE
# DELETE