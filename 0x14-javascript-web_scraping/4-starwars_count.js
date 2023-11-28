#!/usr/bin/node
const request = require('request');
const characterId = '18';
const url = process.argv[2];

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  let movieNum = 0;
  body.data.forEach(movie => {
    movie.characters.forEach(characterUrl => {
      const matchId = characterUrl.match(/\/(\d+)\/$/);
      if (matchId && matchId[1] === characterId) {
        movieNum++;
      }
    });
  });

  console.log(`${movieNum}`);
});
