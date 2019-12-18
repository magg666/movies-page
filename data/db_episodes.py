from data.db_connection import db_connect as con


# CREATE
# READ
@con.connection_handler
def get_episodes_for_season(cursor, season_id):
    sql_str = """
    SELECT id, title, episode_number, overview FROM episodes
    WHERE season_id = %(season_id)s
    """
    cursor.execute(sql_str, {'season_id': season_id})
    episodes_data = cursor.fetchall()
    return episodes_data



# UPDATE
# DELETE