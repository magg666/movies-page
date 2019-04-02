from data import db_shows as shows_manager


def count_all():
    counted_shows = shows_manager.count_series()
    return counted_shows['show_amount']


def get_ordered(number):
    shows_data = shows_manager.get_shows(number)
    for data in shows_data:
        if data['genre_name'][0] is not None:
            data['genre_name'] = ", ".join(data['genre_name'][0:3])
        else:
            data['genre_name'] = None

    return shows_data


