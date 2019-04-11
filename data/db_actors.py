from db_connection import db_connect as con


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


@con.connection_handler
def get_actor_details(cursor, actor_id):
    sql_str = """
    SELECT a.id, a.birthday, a.name, a.death, a.biography FROM actors a
    WHERE a.id = %(actor_id)s
    """
    cursor.execute(sql_str, {'actor_id': actor_id})
    actor_detail = cursor.fetchone()
    return actor_detail
