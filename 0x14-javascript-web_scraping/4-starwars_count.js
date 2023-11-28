#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const characterId = '18';
  const movieNum = body.results.filter(movie => {
    const characterIds = movie.characters.map(characterUrl => {
      const matchId = characterUrl.match(/\/(\d+)\/$/);
      return matchId ? matchId[1] : null;
    });
    return characterIds.includes(characterId);
  });
  console.log(`${movieNum.length}`);
});
