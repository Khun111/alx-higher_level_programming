$(document).ready(() => {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
        data.results.forEach((film) => {
            $('ul#list_movies').append(`<li>${film.title}</li>`);
        });
    });
});

