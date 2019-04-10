import {displayShowsPage} from "./shows.js";
import {addEventListenerToEpisodeButton} from "./episodes.js";
import {sendErrorLogsToServer} from "./communication.js";
import {newDataActors} from "./actors.js";
import {showAddActorModal} from "./add_actor.js";
import {prepareSelectGenre} from "./genres.js";
import {addEventListenerToActor} from "./actors.js";

function main() {
    showAddActorModal();
    if (window.location.pathname === "/") {
        displayShowsPage();
    } else if (window.location.pathname.startsWith("/show/")) {
        addEventListenerToEpisodeButton();
    } else if (window.location.pathname.startsWith("/actors")) {
        newDataActors()
    } else if (window.location.pathname.startsWith("/choose-genre")){
        prepareSelectGenre()
    } else if (window.location.pathname.startsWith("/20-actors")){
        addEventListenerToActor()
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