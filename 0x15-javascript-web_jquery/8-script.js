const list = $('ul#list_movies');

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function (resp) {
    const movies = resp.results;
    $.each(movies, function (index, movie) {
      list.append(`<li>${movie.title}</li>`);
    });
  }
});
