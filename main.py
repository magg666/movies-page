from flask import Flask, render_template, request, jsonify
from data_manager import shows as shows

app = Flask('codecool_series')


@app.route('/')
def index():
    # all_shows = shows.get_ordered(number=0)
    return render_template('index.html')


@app.route('/page', methods=['POST'])
def shows_pages():
    json_number = request.get_json()
    number = json_number['number']
    all_shows = shows.get_ordered(number)
    counted_shows = shows.count_all()
    return jsonify({'shows': all_shows,
                    'counted_shows': counted_shows})


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
