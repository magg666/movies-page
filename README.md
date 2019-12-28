## Movies page
Python | JavaScript | Flask | PostgreSQL | Ajax | CSS
A web page with data about movies, TV series, actors.
Application was based on exam created by CodeCool after Web module.

Created to practice:
* Flask server web application
* Ajax fetching data
* Handling JSON format
* JS template strings
* Arrow functions
* Promises
* Callbacks
* Dynamic DOM manipulations


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Code Examples](#code-examples)
* [Status](#status)
* [Database](#database)
* [Contact](#contact)

## General info
Movie page:
* Shows on main page info about movies and TV series
* Provides pagination
* Allows to filter, sort and select data dynamically
* Shows details about chosen topics

## Technologies
* Python 3.7
* Flask
* Postgresql
* JavaScript
* AJAX
* html, css, bootstrap

## Setup
1. Create a Postgres database and tables for this project using 01_create_schema.sql.
2. Unzip the `data/dump_1000_shows.zip` file
3. Run the unzipped sql files in the following order:
         1. genres
         2. shows
         3. show_genres
         4. seasons
         5. episodes
         6. actors
         7. show_characters
4. Run the server with: *`python main.py`*
Use Pipfile to install all dependencies

## Code Examples
JS promises:
```javascript
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
```
Pagination and events handling:
```javascript
function addPagination() {
    let nextButton = document.getElementById('shows-pagination-next');
    let previousButton = document.getElementById('shows-pagination-previous');

    nextButton.addEventListener('click', function (){
        displayShowsTable(showsParameters.forward)
    });
    previousButton.addEventListener('click', function () {
        displayShowsTable(showsParameters.rewind)
    });
}
```

## Status
Project is finished.

## Database
![Relational model](data/db_schema/relational_model.png?raw=true "Relational model")

## Contact
Created by [Magda Wąsowicz](mailto:mw23127@gmail.com) - feel free to contact me!
