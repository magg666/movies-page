from data import db_episodes as episodes_manager
from log import logging_rules as log


class ReadingProblem(Exception):
    """ If there is problem reading data"""
    pass


def get_all_for_season(season_id):
    try:
        return episodes_manager.get_episodes_for_season(season_id)
    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        raise ReadingProblem


