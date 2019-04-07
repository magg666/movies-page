from flask import Flask, render_template, request, jsonify

from log import logging_rules as log
from data_manager import shows as shows
from data_manager import actors as actors
from data_manager import seasons as seasons
from data_manager import episodes as episodes
from data_manager import genre as genre

app = Flask('codecool_series')


# errors handling
@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('error.html',
                           error=405,
                           error_message='Method not allowed')


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html',
                           error=404,
                           error_message="You will find nothing here. Go home...")


@app.route('/error', methods=['POST'])
def log_js_errors():
    error = request.get_json()
    log.logger.critical('%s', error)


# page routing
@app.route('/')
def index():
    return render_template('shows_table.html')


@app.route('/page', methods=['POST'])
def shows_pages():
    try:
        json_data = request.get_json()
        all_shows = shows.get_ordered(json_data)
        counted_shows = shows.count_all()
        return jsonify({'shows': all_shows,
                        'counted_shows': counted_shows})
    except shows.WrongSort:
        return jsonify({'shows': 'error'})


@app.route('/show/<int:show_id>')
def show(show_id):
    one_show_data = {'one_show': shows.get_one(show_id),
                     'actors': actors.get_for_show(show_id),
                     'seasons': seasons.get_for_show(show_id)}
    return render_template('one_show.html',
                           **one_show_data)


@app.route('/season/<int:season_id>')
def season(season_id):
    try:
        season_data = {'show_title': shows.get_title_by_season_id(season_id),
                       'season_title': seasons.get_title(season_id),
                       'episodes': episodes.get_all_for_season(season_id)}
        return jsonify({'season' + str(season_id): season_data})
    except episodes.ReadingProblem:
        return jsonify({'state': 'error'})


@app.route('/actors')
def top_actors():
    return render_template('actors.html')


@app.route('/actors-list')
def sorted_actors():
    all_actors = actors.get_all_with_shows()
    return jsonify({'actors': all_actors})


@app.route('/actor/<int:actor_id>')
def one_actor(actor_id):
    try:
        one_actor_data = actors.get_one(actor_id)
        return render_template('one_actor.html',
                               actor=one_actor_data,
                               actor_id=actor_id)
    except actors.ReadingProblem:
        message = 'This actor is currently being updated or/and surgically modifying.'
        return render_template('one_actor.html',
                               message=message)


@app.route('/add-actor', methods=['POST'])
def add_actor():
    try:
        actor_data = request.get_json()
        if not actors.is_data_valid(actor_data):
            return jsonify({'state': 'wrong'})
        if actors.is_existing(actor_data):
            return jsonify({'state': 'duplicate'})

        actors.add_new(actor_data)
        return jsonify({'state': 'success'})
    except actors.SavingProblem:
        return jsonify({'state': 'error'})


@app.route('/choose-genre', methods=['GET'])
def show_genres():
    genres = genre.get_all()
    return render_template('select_genre.html',
                           genres=genres)


@app.route('/choose-genre', methods=['POST'])
def search_by_genre():
    genre_id = request.get_json()
    try:
        shows_by_genre = genre.get_shows_by(genre_id)
        return jsonify({'state': shows_by_genre})
    except genre.ReadingProblem:
        return jsonify({'state': 'error'})





@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
