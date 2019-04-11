from data import db_actors as actors_manager
from log import logging_rules as log


class ReadingProblem(Exception):
    """ If there is problem reading data"""
    pass


def get_for_show(show_id):
    try:
        return actors_manager.get_all_actors_for_one_show(show_id)
    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        return []


def get_one(actor_id):
    try:
        return actors_manager.get_actor_details(actor_id)
    except Exception:
        raise ReadingProblem
