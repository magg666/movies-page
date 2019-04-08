import {prepareSelectGenre} from "./genres.js";
import {sendErrorLogsToServer} from "./communication.js";


function main() {
    if (window.location.pathname.startsWith("/choose-genre")) {
        prepareSelectGenre()
    }

}


// error handler
window.addEventListener('error', function (e) {
    let stack = e.error.stack;
    let message = e.error.toString();
    if (stack) {
        message += '\n' + stack;
    }
    sendErrorLogsToServer(message)
});


main();