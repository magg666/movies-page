from db_connection import db_connect as con


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

# UPDATE
# DELETE
