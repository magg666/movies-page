from data.db_connection import db_connect as con


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
def get_episodes_for_season(cursor, season_id):
    sql_str = """
    SELECT id, title, episode_number, overview FROM episodes
    WHERE season_id = %(season_id)s
    ORDER BY episode_number
    """
    cursor.execute(sql_str, {'season_id': season_id})
    episodes_data = cursor.fetchall()
    return episodes_data
