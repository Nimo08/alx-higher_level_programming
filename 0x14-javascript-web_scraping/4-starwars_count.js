#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = '18';

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  let movieNum = 0;
  body.results.forEach(movie => {
    movie.characters.forEach(characterUrl => {
      const matchId = characterUrl.match(/\/(\d+)\/$/);
      if (matchId && matchId[1] === characterId) {
        movieNum++;
      }
    });
  });

  console.log(`${movieNum}`);
});
