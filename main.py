from flask import Flask, render_template, request, jsonify

from data_manager import shows as shows
from data_manager import actors as actors
from data_manager import seasons as seasons

app = Flask('codecool_series')


@app.route('/')
def index():
    return render_template('shows_table.html')


@app.route('/page', methods=['POST'])
def shows_pages():
    json_data = request.get_json()
    all_shows = shows.get_ordered(json_data)
    counted_shows = shows.count_all()
    return jsonify({'shows': all_shows,
                    'counted_shows': counted_shows})


@app.route('/show/<int:show_id>')
def show(show_id):
    one_show_data = {'one_show': shows.get_one(show_id),
                     'actors': actors.get_for_show(show_id),
                     'seasons': seasons.get_for_show(show_id)}
    return render_template('one_show.html',
                           **one_show_data)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
