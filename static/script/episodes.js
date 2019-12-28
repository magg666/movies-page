import {getData, postData} from "./communication.js";
import {formatDataOfEpisodes} from "./data_formatter.js";
import {openModal} from "./dom.js";

export {addEventListenerToEpisodeButton}


function addEventListenerToEpisodeButton() {
    let allButtons = document.querySelectorAll('.episodes');
    for (let button of allButtons) {
        button.addEventListener('click', displayEpisodesModal.bind(null, button))
    }
}

function displayEpisodesModal(button) {
    let seasonId = parseInt(button.dataset.seasonId, 10);
    getData(`/season/${seasonId}`, checkEpisodesData)

}
function checkEpisodesData(data) {
    if(data['state'] === 'error'){
        openModal('user', 'We are very sorry, but some error happened. Try again later' )
    }
    else {
        createEpisodesModal(data)
    }
}


function createEpisodesModal(data) {
    let modalContainer = document.getElementById('episodes-modal-container');
    modalContainer.innerHTML = '';
    modalContainer.classList.toggle('visible');

    let formattedData = formatDataOfEpisodes(data);
    let allEpisodes = '';

    for (let episode of formattedData.episodes) {
        episode = `

        <p class="episodes-modal-title">Number of episode: ${episode['episode_number']}
        <span class="separator">|</span class="episodes-modal-title">${episode['title']}</p>
        <p>${episode['overview']}</p>
        <hr class="line">     

        `;
        allEpisodes += episode
    }

    let modal = `
    <div class="episodes-modal-body card">
        <div class="episodes-modal-title">
            <button class="episodes-modal-close"><span>&times;</span></button>
            <span>${formattedData['show_title']}</span>
            <span class="separator">|</span>
            <span>${formattedData['season_title']}</span>
        </div>
        <hr class="line">        
        <div class="episodes-modal-message">
            <div class="episodes">${allEpisodes}</div>
        </div>
    </div>
    `;
    modalContainer.insertAdjacentHTML("afterbegin", modal);
    addHidingModal(modalContainer)
}

function addHidingModal(modal) {
    let closeButton = document.querySelector('.episodes-modal-close');
    closeButton.addEventListener('click', closeModal.bind(null, modal));
    // setTimeout(function () {
    //     window.addEventListener('click', closeModal.bind(null, modal))
    // }, 200)
}

function closeModal(modal) {
    modal.innerHTML = "";
    // window.removeEventListener('click', function (){
    //     closeModal(modal)
    // }, true);
    modal.classList.remove('visible');

}