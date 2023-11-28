#!/usr/bin/node
const arg = process.argv[2];
const fs = require('fs');
fs.readFile(arg, 'utf8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});
