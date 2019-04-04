export {formatShowsData}

function formatShowsData(data) {
    return {
        countedShows: data['counted_shows'],
        allShows: data['shows'].map(show => {
            let id = show['id'],
                title = show['title'],
                year = show['year'],
                runtime = show['runtime'] + ' min.',
                genres = show['genre_name'] !== null ? show['genre_name']: 'Suggest genre!'.fontcolor('red'),
                rating = Number.parseFloat(show['rating']).toFixed(2),
                homepage = show['homepage'] !== null ? `<a href="${show['homepage']}" target="_blank">${title} homepage</a>` : 'unknown',
                trailer = show['trailer'] !== null ? `<a href="${show['trailer']}" target="_blank">${title} trailer</a>` : 'unknown';
            return [id, title, year, runtime, genres, rating, homepage, trailer]
        })
    };
}
