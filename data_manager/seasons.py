from data import db_seasons as seasons_manager
from log import logging_rules as log


class ReadingProblem(Exception):
    """ If there is problem reading data"""
    pass


def get_for_show(show_id):
    try:
        seasons = seasons_manager.get_seasons_for_show(show_id)
        for season in seasons:
            if season['overview'] is None:
                if season['title'] == 'Specials':
                    season['overview'] = 'Trailers, one-time movies, behind scenes and many more...'
                else:
                    season['overview'] = 'This season do not has a overview yet. Join us and write your own summary!'
        return seasons
    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        return []


def get_all_episodes_for_season(season_id):
    try:
        return seasons_manager.get_episodes_for_season(season_id)
    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        raise ReadingProblem
