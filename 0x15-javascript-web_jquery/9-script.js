// Script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello
// The translation of “hello” must be displayed in the HTML tag DIV#hello

$(document).ready(function () {
  const urlApi = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.ajax({
    url: urlApi,
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      $('#hello').text(data.hello);
    },
    error: (error) => {
      console.error('API call failed', error);
    }
  });
});
