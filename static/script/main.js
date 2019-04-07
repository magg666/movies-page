import {displayShowsPage} from "./shows.js";
import {addEventListenerToEpisodeButton} from "./episodes.js";
import {sendErrorLogsToServer} from "./communication.js";
import {newDataActors} from "./actors.js";

function main() {

    if (window.location.pathname === "/") {
        displayShowsPage();
    } else if (window.location.pathname.startsWith("/show/")) {
        addEventListenerToEpisodeButton();
    } else if (window.location.pathname.startsWith("/actors")) {
        newDataActors()
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