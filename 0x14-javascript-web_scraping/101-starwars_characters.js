#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // array for character names
  const charNames = [];

  // recursive function to fetch character names sequentially
  function fetchChar (index) {
    if (index >= body.characters.length) {
      charNames.forEach(name => console.log(name));
      return;
    }

    const charUrl = body.characters[index];
    request(charUrl, { json: true }, (error, response, character) => {
      if (error) {
        console.error(error);
      } else {
        charNames.push(character.name);
      }

      fetchChar(index + 1);
    });
  }

  fetchChar(0);
});
