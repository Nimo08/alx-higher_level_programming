#!/usr/bin/node
const process = require('process');
const x = parseInt(process.argv[2], 10);
if (x) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
