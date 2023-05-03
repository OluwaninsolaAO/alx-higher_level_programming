const myDiv = $('div#character');

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  success: function (character) {
    myDiv.text(character.name);
  }
});
