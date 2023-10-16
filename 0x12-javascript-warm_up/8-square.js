#!/usr/bin/node
const process = require('process');
const arg = parseInt(process.argv[2], 10);
if (arg) {
  for (let i = 0; i < arg; i++) {
    let square = ''; // build rows
    for (let j = 0; j < arg; j++) {
      square += 'X'; // append X to rows
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
