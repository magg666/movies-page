import {postData} from "./communication.js";
import {openModal} from "./dom.js";

export {showAddActorModal}


function showAddActorModal() {
    const addActorTrigger = document.getElementById('new-actor');
    addActorTrigger.addEventListener('click', createActorModal)
}


function createActorModal(data) {
    let modalContainer = document.getElementById('actor-modal-container');
    modalContainer.innerHTML = '';
    modalContainer.classList.toggle('visible');

    let addActorModal = `
    <div class="actor-modal-body card">
        <div class="actor-modal-title">
            <button class="actor-modal-close"><span>&times;</span></button>
            <span>Add new actor</span>
        </div>
        <hr class="line">        
        <div class="actor-modal-message">
        <form role="form" id="add-actor-form" class="form" autocomplete="off">
            <label>Actor's name
            <p><input id="actor-name" required></p></label>
            <label>Actor's birthday date
            <p><input id="actor-birthday" pattern="^\\d{4}-\\d{2}-\\d{2}$" placeholder="rrrr-mm-dd" required></p></label>
            <label>Actor's death date (if valid)
            <p><input id="actor-death" placeholder="rrrr-mm-dd or leave empty"></p></label>
            <label>Actor's biography
            <p><textarea id="actor-biography" placeholder="min. 20 signs" required></textarea></p></label>
            <p><button type="submit">Add actor</button></p>
         </form>   
        </div>
        
    </div>
    `;


    modalContainer.insertAdjacentHTML("afterbegin", addActorModal);
    addHideActorModal(modalContainer);
    addValidationToForm()
}

function addHideActorModal(modal) {
    let closeButton = document.querySelector('.actor-modal-close');
    closeButton.addEventListener('click', closeModal.bind(null, modal));
}

function closeModal(modal) {
    modal.innerHTML = "";
    modal.classList.remove('visible');
}

function informUserIfActorAdded(response) {
    if (response['state'] === 'success') {
        openModal('user', 'Your actor is added. Thank you for contribution')
    } else if (response['state'] === 'duplicate') {
        openModal('user', 'Sorry, this actor is already in database.')
    } else if (response['state'] === 'error') {
        openModal('user', 'Your actor will be verified and added in 24h. Thank you.')
    } else if (response['state'] === 'wrong'){
        openModal('user', 'You provided wrong data for actor. Sorry, but you can try again')
    }
}


function addValidationToForm() {
    let actorModal = document.getElementById('actor-modal-container');
    let form = document.getElementById('actor-modal-container');
    form.addEventListener('submit', function (ev) {
        ev.preventDefault();
        if (formValidated(form)) {
            let actorData = {
                'actor_name': form.querySelector('#actor-name').value,
                'actor_birthday': form.querySelector('#actor-birthday').value,
                'actor_death': form.querySelector('#actor-death').value,
                'actor_biography': form.querySelector('#actor-biography').value,

            };
            closeModal(actorModal);
            postData('/add-actor', actorData, informUserIfActorAdded);
        }
    })
}

function formValidated(form) {
    if (validateDeathField(form) &&
        validateRequiredInputs(form)) {
        return true
    }
}

function validateDeathField(form) {
    let deathField = form.querySelector('#actor-death');
    let deathFieldValid = true;
    let datePattern = "^\\d{4}-\\d{2}-\\d{2}$";
    const properDateFormat = new RegExp(datePattern, 'gi');

    if (!properDateFormat.test(deathField.value) && deathField.value.trim() !== '') {
        deathFieldValid = false
    }
    if (deathFieldValid) {
        showValidation(deathField, true);
        return true;
    } else {
        showValidation(deathField, false);
        return false;
    }
}

function validateRequiredInputs(form) {
    let actorName = form.querySelector('#actor-name');
    let actorBirthday = form.querySelector('#actor-birthday');
    let actorBiography = form.querySelector('#actor-biography');
    if (validateRequiredInput(actorName)
        && validateRequiredInput(actorBirthday)
        && validateTextArea(actorBiography)) {
        return true
    }
}

function validateRequiredInput(input) {
    let inputIsValid = true;
    const pattern = input.getAttribute('pattern');

    if (pattern !== null) {
        const properDateFormat = new RegExp(pattern, 'gi');
        if (!properDateFormat.test(input.value)) {
            inputIsValid = false;
        }
    } else {
        if (input.value === '') {
            inputIsValid = false;
        }
    }
    if (inputIsValid) {
        showValidation(input, true);
        return true;
    } else {
        showValidation(input, false);
        return false;
    }
}

function validateTextArea(textarea) {
    let textareaIsValid = true;
    if (textarea.value.length < 20 || textarea.value.trim() === '') {
        textareaIsValid = false
    }
    if (textareaIsValid) {
        showValidation(textarea, true);
        return true
    } else {
        showValidation(textarea, false);
        return false
    }
}

function showValidation(input, inputIsValid) {
    if (!inputIsValid) {
        input.classList.add('error');
    } else {
        input.classList.remove('error');
    }
}

