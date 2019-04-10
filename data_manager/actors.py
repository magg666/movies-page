from datetime import datetime

from data import db_actors as actors_manager
from log import logging_rules as log


class ReadingProblem(Exception):
    """ If there is problem with reading data"""
    pass


class SavingProblem(Exception):
    """ If there is problem with saving data"""
    pass


def get_for_show(show_id):
    try:
        return actors_manager.get_all_actors_for_one_show(show_id)
    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        return []


def get_all_with_shows():
    try:
        return actors_manager.get_all_actors_with_shows()

    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        raise ReadingProblem


def get_one(actor_id):
    try:
        one_actor = actors_manager.get_one_actor(actor_id)
        if one_actor['death'] is None:
            one_actor['death'] = 'still alive'
            return one_actor
    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        raise ReadingProblem


def is_data_keys_valid(actor_data):
    if 'actor_name' in actor_data and \
            'actor_birthday' in actor_data and \
            'actor_death' in actor_data and \
            'actor_biography' in actor_data:
        return True
    else:
        return False


def is_existing(actor_data):
    try:
        return actors_manager.exists_already(actor_data['actor_name'])
    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        raise ReadingProblem


def check_actors_name(actor_data):
    if actor_data['actor_name'].strip() != '':
        return True


def check_actors_birth(actor_data):
    try:
        if datetime.strptime(actor_data['actor_birthday'], '%Y-%m-%d'):
            return True
    except ValueError:
        return False


def check_actors_death(actor_data):
    try:
        if actor_data['actor_death'] == '' or datetime.strptime(actor_data['actor_death'], '%Y-%m-%d'):
            return True
    except ValueError:
        return False


def check_actors_biography(actor_data):
    return len(actor_data['actor_biography']) > 20


def is_data_valid(actor_data):
    if is_data_keys_valid(actor_data) and \
            check_actors_name(actor_data) and \
            check_actors_birth(actor_data) and \
            check_actors_death(actor_data) and \
            check_actors_biography(actor_data):
        return True


def add_new(actor_data):
    try:
        if actor_data['actor_death'] == '':
            actor_data['actor_death'] = None

        actors_manager.add_new_actor(actor_data)

    except Exception as err:
        log.logger.error(
            '{0}, Data to be added: {actor_name}/{actor_birthday}/{actor_death}/{actor_biography}'.format(err,
                                                                                                          **actor_data))
        log.logging.exception(err)
        raise SavingProblem


def get_twenty_with_shows():
    try:
        return actors_manager.get_twenty_actors_with_shows()
    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        raise ReadingProblem


def get_shows_for_actor(actor_id):
    try:
        return actors_manager.get_shows_for_actor(actor_id)
    except Exception as err:
        log.logger.error('%s', err)
        log.logging.exception(err)
        raise ReadingProblem
