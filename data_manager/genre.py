from data import db_genre as genre_manager
from log import logging_rules as log


class ReadingProblem(Exception):
    """ If there is problem reading data"""
    pass


def get_all():
    return genre_manager.get_all_genres()


def get_shows_by(genre_id):
    try:
        real_genre_id = genre_id['genre_id']
        return genre_manager.get_shows_by_genre_id(real_genre_id)
    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        raise ReadingProblem

