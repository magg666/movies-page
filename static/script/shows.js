import {postData, getData} from "./communication.js";
import {formatShowsData} from "./data_formatter.js";
import {clearElement} from "./dom.js";

export {displayShowsPage}

let showsParameters = {
    allShows: '',
    forward: 15,
    rewind: -15,
    offsetForShows: 0,
};

function displayShowsTable(way=0) {
    showsParameters.offsetForShows += way;
    let pageNumber = {
        'number': showsParameters.offsetForShows
    };
    postData('/page', pageNumber, createShowsTable);
    return showsParameters.offsetForShows
}

function addPagination() {
    let nextButton = document.getElementById('shows-pagination-next');
    let previousButton = document.getElementById('shows-pagination-previous');

    nextButton.addEventListener('click', function (){
        displayShowsTable(showsParameters.forward)
    });
    previousButton.addEventListener('click', function () {
        displayShowsTable(showsParameters.rewind)
    });
}

function cannotRewind() {
    return showsParameters.offsetForShows + showsParameters.rewind < 0
}

function cannotForward() {
    return showsParameters.offsetForShows + showsParameters.forward >= showsParameters.allShows
}

function checkDisplayingPaginationButtons() {
    let nextButton = document.getElementById('shows-pagination-next');
    let previousButton = document.getElementById('shows-pagination-previous');

    previousButton.disabled = false;
    nextButton.disabled = false;
    if(cannotRewind()){
        previousButton.disabled = true
    }
    if(cannotForward()){
        nextButton.disabled = true
    }
}

function createShowsTable(data) {
    let showsTableBody = document.getElementById('shows-table-body');
    let formattedShows = formatShowsData(data);
    showsParameters.allShows = formattedShows.countedShows;
    checkDisplayingPaginationButtons();

    clearElement(showsTableBody);

    for (let show of formattedShows['allShows']) {
        let allCells = '';
        let cell = '';
        for (let i = 1; i < show.length; i++) {
            if (i === 1) {
                cell = `<td><a href="/show/${show[0]}">${show[i]}</a></td>`;
            } else {
                cell = `<td>${show[i]}</td>`
            }
            allCells += cell
        }
        let row = `<tr>${allCells}</tr>`;

        showsTableBody.insertAdjacentHTML('beforeend', row)
    }
}

function displayShowsPage() {
    displayShowsTable();
    addPagination();
}