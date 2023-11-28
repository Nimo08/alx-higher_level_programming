#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
// get content of webpage
request.get(url, { encoding: 'utf8' }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  // write body to file
  fs.writeFile(filePath, body, 'utf8', err => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(`${filePath}`);
  });
});
