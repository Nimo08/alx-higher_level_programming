#!/usr/bin/node
const process = require('process');
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    const sum = a + b;
    console.log(sum);
  }
}
const arg1 = parseInt(process.argv[2], 10);
const arg2 = parseInt(process.argv[3], 10);
add(arg1, arg2);
