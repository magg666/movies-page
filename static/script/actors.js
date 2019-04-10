import {getData, postData} from "./communication.js";
import {openModal} from "./dom.js";

export {newDataActors, addEventListenerToActor}

let actorsParameters = {
    allActors: '',
    startIndex: 0,
    endIndex: 20,
    forward: 20,
    rewind: -20,

};

//---- preparing actors data

// a) sorting
function sortActorsData(data) {
    let sortable = [];
    for (let key in data['actors']) {
        if (data['actors'].hasOwnProperty(key)) {
            sortable.push(data['actors'][key]);
        } else {
            openModal('user', 'Page is under construction. Try again later')
        }
    }
    sortable.sort(function (a, b) {
        if (a['name'] && b['name']) {
            return a['name'].localeCompare(b['name']);
        }


    });
    actorsParameters.allActors = sortable.length;
    return sortable
}

// b) cutting to 20 from sorted data
function prepareActorsData(data) {
    data = sortActorsData(data);
    let newData = data.slice(actorsParameters.startIndex, actorsParameters.endIndex);
    createActorsTable(newData)
}


// function to get data from server
function getActorsData() {
    getData('/actors-list', prepareActorsData);
}

// ----------------

function displayActorsTable(way = 0) {
    actorsParameters.startIndex += way;
    actorsParameters.endIndex += way;
    getActorsData();
}

function newDataActors() {
    displayActorsTable(0);
    addActorPagination();
}


function createActorsTable(data) {
    let actorContainer = document.getElementById('actors-page');
    actorContainer.innerHTML = "";
    checkDisplayingPaginationButtons();

    for (let actor of data) {
        let actorsShows = '';
        for (let key in actor['shows_object']) {
            if (actor['shows_object'].hasOwnProperty(key)) {
                let value = actor['shows_object'][key];
                let linkAndShowTitle = `<a href="/show/${key}"><span>${value}</span></a><span class="separator">|</span>`;
                actorsShows += linkAndShowTitle;
            }
        }
        let actorRow = `
                <tr>
                    <td><a href="/actor/${actor['id']}">${actor['name']}</a></td>
                    <td> ${actorsShows}
                    </td>
                </tr>`;
        actorContainer.insertAdjacentHTML("beforeend", actorRow)
    }

}

// pagination
function addActorPagination() {
    let nextButton = document.getElementById('actors-pagination-next');
    let previousButton = document.getElementById('actors-pagination-previous');

    nextButton.addEventListener('click', function () {
        displayActorsTable(actorsParameters.forward)
    });
    previousButton.addEventListener('click', function () {
        displayActorsTable(actorsParameters.rewind)
    });
}

function cannotRewind() {
    return actorsParameters.startIndex + actorsParameters.rewind < 0
}

function cannotForward() {
    return actorsParameters.startIndex + actorsParameters.forward >= actorsParameters.allActors
}

function checkDisplayingPaginationButtons() {
    let nextButton = document.getElementById('actors-pagination-next');
    let previousButton = document.getElementById('actors-pagination-previous');

    previousButton.disabled = false;
    nextButton.disabled = false;
    if (cannotRewind()) {
        previousButton.disabled = true
    }
    if (cannotForward()) {
        nextButton.disabled = true
    }
}


//-----

function getShowsForActor(actor) {
    let actorId = actor.dataset.actorId;
    postData(`/actor-info/${actorId}`, actorId, showActorsWithShows)
}

function showActorsWithShows(responseData) {
    if(responseData['shows'] === []){
        openModal('user', "No actor's info")
    }else{
        createModalWithShowsOfActor(responseData['shows'])
    }

}

function createModalWithShowsOfActor(data) {
    let modalContainer = document.getElementById('actor-details-modal');
    modalContainer.classList.add('visible');
    modalContainer.innerHTML = "";
    let allOfShows ='';
    for(let show of data){
        let row = `<li><a href="/show-page/${show['id']}">${show['title']}</a></li>`;
        allOfShows += row
    }

    let actorModal = `
   <div class="actor-modal-body card">
        <div class="actor-modal-title">
            <button class="actor-modal-close" id="close-actor"><span>&times;</span></button> 
        </div>          
            <hr class="line">  
        <div class="episodes-modal-message">
           <ul>${allOfShows}</ul> 
        </div>
    </div>`;
    modalContainer.insertAdjacentHTML("beforeend", actorModal);
    addHidingModal(modalContainer)
}

function addEventListenerToActor() {
    let allActorsLinks = document.querySelectorAll('.actor');
    for(let actor of allActorsLinks){
        actor.addEventListener('click', function (ev) {
            ev.preventDefault();
            getShowsForActor(actor)
        })
    }
}

function addHidingModal(modal) {
    let closeButton = document.getElementById('close-actor');
    closeButton.addEventListener('click', function () {
        modal.classList.remove('visible')
    })
}