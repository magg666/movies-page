import {formatShowsData} from "./data_formatter.js";
export {clearElement, openModal}

function clearElement(element){
    element.innerHTML = '';
}
function createSmallModal(username, message) {
    let modalContainer = document.getElementById('small-modal');
    let modal = `
    <div class="info-modal-body">
        <div class="info-modal-title">
            <button class="info-modal-close" id="close-small-modal"><span>&times;</span></button>
            <span>Hello <strong>${username}</strong></span>
        </div>        
        <div class="info-modal-message">
            <span>${message}</span>
        </div>
    </div>
    `;
    modalContainer.insertAdjacentHTML("afterbegin", modal)
}

function openModal(username='user', message) {
    createSmallModal(username, message);
    let modal = document.getElementById('small-modal');
    modal.classList.replace('hidden', 'visible');
    addHidingModal();
}

function closeSmallModal() {
    let modal = document.getElementById('small-modal');
    modal.innerHTML = "";
    modal.classList.replace('visible', 'hidden');
    window.removeEventListener('click', closeSmallModal)
}

function addHidingModal() {
    let closeButton = document.getElementById('close-small-modal');
    closeButton.addEventListener('click', closeSmallModal);
    setTimeout(function () {
        window.addEventListener('click', closeSmallModal)
    }, 200)
}
