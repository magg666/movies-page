from data import db_actors as actors_manager


def get_for_show(show_id):
    actors = actors_manager.get_all_actors_for_one_show(show_id)
    return actors


