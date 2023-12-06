// Script that fetches and lists the title for all movies by using this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies

$(document).ready(function () {
  const urlApi = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.ajax({
    url: urlApi,
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      const movies = data.results;
      const $moviesList = $('#list_movies');
      movies.forEach(function (movie) {
        $moviesList.append('<li>' + movie.title + '</li>');
      });
    },
    error: (error) => {
      console.error('API call failed', error);
    }
  });
});
