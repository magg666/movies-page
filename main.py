from flask import Flask, render_template, request, jsonify

from data import queries
from data_manager import genres as genre

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


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
