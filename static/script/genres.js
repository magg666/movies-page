import {postData} from "./communication.js";
import {openModal} from "./dom.js";

export {prepareSelectGenre}



function validateChosenGenre(select) {
    if(select.options[select.selectedIndex].value === '-1'){
        showValidation(select, false);
        return false
    } else {
        showValidation(select, true);
        return true
    }
}


function prepareSelectGenre(){
    let selectForm = document.getElementById('choose-genre');
    selectForm.addEventListener('change', function () {
        if(validateChosenGenre(selectForm)){
            let genreId = {
                'genre_id': selectForm.options[selectForm.selectedIndex].value
            };
            postData('/choose-genre', genreId, handleResponse)
        }
    })
}

function handleResponse(response) {
    if(response['state'] === 'error'){
        openModal('user', 'Searching by genre is now modernised. Try again later')
    } else {
        displayShowsByGenre(response['state'])
    }
}

function displayShowsByGenre(showsData){
    let showsContainer = document.getElementById('search-results');
    showsContainer.innerHTML = "";

    for(let show of showsData){
        let showRow = `
                    <tr>
                    <td>${show['title']}</td>
                    <td>${show['rating']}</td>
                    <td>${show['year']}</td>
                    </tr>`;
        showsContainer.insertAdjacentHTML('beforeend', showRow)
    }

}

function showValidation(input, inputIsValid) {
    if (!inputIsValid) {
        input.classList.add('error');
    } else {
        input.classList.remove('error');
    }
}