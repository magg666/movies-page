from flask import Flask, render_template, request, jsonify, redirect

from data import queries
from data_manager import genres as genre
from data_manager import shows as shows
from data_manager import actors as actors
from data_manager import seasons as seasons


app = Flask('codecool_series')


@app.route('/')
def index():
    all_shows = queries.get_shows()
    return render_template('index.html', shows=all_shows)


@app.route('/tv-show/<int:show_id>')
def show_show(show_id):
    one_show_data = {'one_show': shows.get_one(show_id),
                     'actors': actors.get_for_show(show_id),
                     'seasons': seasons.get_for_show(show_id)}
    return render_template('one_show.html',
                           **one_show_data)


@app.route('/season-episodes/<int:season_id>')
def show_episodes_for_season(season_id):
    try:
        episodes = seasons.get_all_episodes_for_season(season_id)
        return render_template('episodes.html', episodes=episodes)
    except seasons.ReadingProblem:
        return redirect('/') # Here should be some info for user that page is broken


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


@app.route('/actor/<int:actor_id>')
def show_actor_detail(actor_id):
    try:
        one_actor = actors.get_one(actor_id)
        return render_template('one_actor.html',
                               one_actor=one_actor)
    except actors.ReadingProblem:
        return redirect('/')




@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
