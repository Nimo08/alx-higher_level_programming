#!/usr/bin/node
const arg = process.argv[2];
const line = process.argv[3];
const fs = require('fs');
fs.writeFile(arg, line, 'utf8', error => {
  if (error) {
    console.error(error);
  }
});
