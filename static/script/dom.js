import {formatShowsData} from "./data_formatter.js";
export {clearElement}

function clearElement(element){
    while (element.firstChild){
        element.removeChild(element.firstChild)
    }
}
