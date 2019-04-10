from db_connection import db_connect as con


# CREATE
@con.connection_handler
def add_new_actor(cursor, actor_data):
    sql_str = """
    INSERT INTO actors(name, birthday, death, biography)
    VALUES (%(actor_name)s, %(actor_birthday)s, %(actor_death)s, %(actor_biography)s)
    """
    cursor.execute(sql_str, {'actor_name': actor_data['actor_name'],
                             'actor_birthday': actor_data['actor_birthday'],
                             'actor_death': actor_data['actor_death'],
                             'actor_biography': actor_data['actor_biography']})


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
    SELECT a.name, a.id, COALESCE(json_object_agg(DISTINCT s.id, s.title) FILTER ( WHERE s.id IS NOT NULL ), '{}') as shows_object
FROM actors a
       FULL OUTER JOIN show_characters sc on a.id = sc.actor_id
       FULL OUTER JOIN shows s on sc.show_id = s.id
GROUP BY a.name, a.id
    """

    cursor.execute(sql_str)
    actors_with_shows = cursor.fetchall()
    return actors_with_shows


@con.connection_handler
def get_one_actor(cursor, actor_id):
    sql_str = """
    SELECT a.name, a.birthday, a.death, a.biography, 
    COALESCE(json_object_agg(sc.character_name, s.title) 
    FILTER ( WHERE sc.character_name IS NOT NULL ), '{}') as show_role
    FROM actors a
       FULL OUTER JOIN show_characters sc on a.id = sc.actor_id
       FULL OUTER JOIN shows s on sc.show_id = s.id
    WHERE a.id = %(actor_id)s
    GROUP BY a.name, a.birthday, a.death, a.biography
    """
    cursor.execute(sql_str, {'actor_id': actor_id})
    one_actor = cursor.fetchone()
    return one_actor


@con.connection_handler
def exists_already(cursor, actor_name):
    sql_str = """
    SELECT EXISTS(SELECT 1
                     FROM actors
                     WHERE actors.name = %(actor_name)s)
    """
    cursor.execute(sql_str, {'actor_name': actor_name})
    exist = cursor.fetchone()
    return exist['exists']


# UPDATE
# DELETE
@con.connection_handler
def delete_actor(cursor, actor_id):
    sql_str = """
    DELETE FROM show_characters
    WHERE actor_id = %(actor_id)s;
    DELETE FROM actors
    WHERE id = %(actor_id)s
    RETURNING actors.name
    """
    cursor.execute(sql_str, {'actor_id': actor_id})
    deleted_name = cursor.fetchone()
    return deleted_name


@con.connection_handler
def get_twenty_actors_with_shows(cursor):
    sql_str = """
    SELECT a.name, string_agg(DISTINCT s.title, ' | ') FROM actors a
    LEFT JOIN show_characters sc on a.id = sc.actor_id
    LEFT JOIN shows s on sc.show_id = s.id
    GROUP BY a.name
    ORDER BY a.name ASC
    LIMIT 20
    """
    cursor.execute(sql_str)
    all_actors_with_shows = cursor.fetchall()
    return all_actors_with_shows
