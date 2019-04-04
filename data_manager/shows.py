from data import db_shows as shows_manager


def count_all():
    counted_shows = shows_manager.count_series()
    return counted_shows['show_amount']


def get_ordered(json_data):
    number = json_data['number']
    sort_by = json_data['sort_by']
    order = json_data['order']

    shows_data = shows_manager.get_shows(number, sort_by, order)
    for data in shows_data:
        if data['genre_name'] is not None:
            data['genre_name'] = ", ".join((data['genre_name'].split(' '))[0:3])

    return shows_data


def get_one(show_id):
    one_show = shows_manager.get_one_show(show_id)

    if one_show['trailer']:
        one_show['trailer'] = one_show['trailer'].replace('watch?v=', 'embed/')
    return one_show

