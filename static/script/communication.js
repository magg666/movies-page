export {getData, postData}

function getData(link, callback) {
    fetch(link, {
        method: 'GET'
    })
        .then(response => response.json())
        .then(json_response => callback(json_response))
//        .catch(error => sendErrorLogsToServer(error.message + error.stack))
        .catch(error => console.log(error))
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
  //      .catch(error => sendErrorLogsToServer(error.message + error.stack))
        .catch(error => console.log(error))
}

// proste wysyłanie daych na server - logi błędów
function sendErrorLogsToServer(error) {
    let errorRequest = new XMLHttpRequest();
    errorRequest.open("POST", "/error");
    errorRequest.setRequestHeader("Content-type", "application/json");
    errorRequest.send(JSON.stringify(error))
}