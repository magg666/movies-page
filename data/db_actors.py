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


@con.connection_handler
def get_all_actors_with_shows(cursor):
    sql_str = """
    SELECT a.name, a.id, json_object_agg(DISTINCT s.id, s.title) as shows_object FROM actors a
    JOIN show_characters sc on a.id = sc.actor_id
    JOIN shows s on sc.show_id = s.id
    GROUP BY a.name, a.id
    """

    cursor.execute(sql_str)
    actors_with_shows = cursor.fetchall()
    return actors_with_shows


@con.connection_handler
def get_one_actor(cursor, actor_id):
    sql_str = """
    SELECT a.name, a.birthday, a.death, a.biography, json_object_agg(sc.character_name, s.title) as show_role
    FROM actors a
       JOIN show_characters sc on a.id = sc.actor_id
       JOIN shows s on sc.show_id = s.id
    WHERE a.id = %(actor_id)s
    GROUP BY a.name, a.birthday, a.death, a.biography
    """
    cursor.execute(sql_str, {'actor_id': actor_id})
    one_actor = cursor.fetchone()
    return one_actor

# UPDATE
# DELETE
