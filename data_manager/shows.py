from log import logging_rules as log
from data import db_shows as shows_manager


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
