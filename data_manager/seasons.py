from data import db_seasons as seasons_manager


def get_for_show(show_id):
    seasons = seasons_manager.get_seasons_for_show(show_id)
    for season in seasons:
        if season['overview'] is None:
            if season['title'] == 'Specials':
                season['overview'] = 'Trailers, one-time movies, behind scenes and many more...'
            else:
                season['overview'] = 'This season do not has a overview yet. Join us and write your own summary!'
    return seasons
