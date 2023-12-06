// Script that fetches the character name from this URL:
// https://swapi-api.alx-tools.com/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character

$(document).ready(function () {
  const urlApi = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.ajax({
    url: urlApi,
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      $('#character').text(data.name);
    },
    error: (error) => {
      console.error('API call failed', error);
    }
  });
});
