from log import logging_rules as log
from data import db_shows as shows_manager


class WrongSort(Exception):
    """ If there is problem with sort functions"""
    pass


class ReadingProblem(Exception):
    """ If there is problem reading data"""
    pass


def count_all():
    counted_shows = shows_manager.count_series()
    return counted_shows['show_amount']


def get_ordered(json_data):
    try:
        number = json_data['number']
        sort_by = json_data['sort_by']
        order = json_data['order']
        shows_data = shows_manager.get_shows(number, sort_by, order)
        for data in shows_data:
            if data['genre_name'] is not None:
                data['genre_name'] = ", ".join((data['genre_name'].split(' '))[0:3])

        return shows_data

    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        raise WrongSort


def get_one(show_id):
    try:
        one_show = shows_manager.get_one_show(show_id)
        if one_show['trailer']:
            one_show['trailer'] = one_show['trailer'].replace('watch?v=', 'embed/')
        if one_show['year']:
            one_show['year'] = int(one_show['year'])
        return one_show
    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        return {}


def get_title_by_season_id(season_id):
    try:
        show_title = shows_manager.get_show_title_by_season(season_id)
        return show_title['title']
    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        return ""
