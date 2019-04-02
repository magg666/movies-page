from db_connection import data_manager
from db_connection import db_connect as con


@con.connection_handler
def get_shows(cursor):
    sql_str = """
    SELECT id, title,year, runtime, rating FROM shows
    ORDER BY rating
    LIMIT 15
    
    """
    cursor.execute(sql_str)
    all_shows = cursor.fetchall()
    return all_shows
