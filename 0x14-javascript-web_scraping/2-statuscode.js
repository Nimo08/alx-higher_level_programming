#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];
request.get(arg, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
