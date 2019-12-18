from data.db_connection import db_connect as con


# CREATE
# READ
@con.connection_handler
def get_seasons_for_show(cursor, show_id):
    sql_str = """
    SELECT * FROM seasons
    WHERE show_id = %(show_id)s
    ORDER BY season_number
    """
    cursor.execute(sql_str, {'show_id': show_id})
    return cursor.fetchall()


@con.connection_handler
def get_season_title_by_id(cursor, season_id):
    sql_str = """
    SELECT title FROM seasons
    WHERE id = %(season_id)s
    """
    cursor.execute(sql_str, {'season_id': season_id})
    season_title = cursor.fetchone()
    return season_title

# UPDATE
# DELETE
