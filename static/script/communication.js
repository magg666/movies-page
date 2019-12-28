export {getData, postData, sendErrorLogsToServer}
import {openModal} from "./dom.js";

function getData(link, callback) {
    fetch(link, {
        method: 'GET'
    })
        .then(response => response.json())
        .then(json_response => callback(json_response))
        .catch(error => {
            openModal('user', 'Sorry, this page is under work. Try again later');
            sendErrorLogsToServer(error.message + error.stack);
        })
}

function postData(link, data, callback) {
    fetch(link, {
        method: 'POST',
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(json_response => callback(json_response))
        .catch(error => {
            openModal('user', 'Sorry, this page is under work. Try again later');
            sendErrorLogsToServer(error.message + error.stack);
        })
}

// proste wysyłanie daych na server - logi błędów
function sendErrorLogsToServer(error) {
    let errorRequest = new XMLHttpRequest();
    errorRequest.open("POST", "/error");
    errorRequest.setRequestHeader("Content-type", "application/json");
    errorRequest.send(JSON.stringify(error))
}