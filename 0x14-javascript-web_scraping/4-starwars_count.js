#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movieNum = body.results.filter(movie =>
    movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );
  console.log(`${movieNum.length}`);
});
