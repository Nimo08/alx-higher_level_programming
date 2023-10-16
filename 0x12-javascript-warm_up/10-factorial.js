#!/usr/bin/node
const process = require('process');
const arg = parseInt(process.argv[2], 10);
function factorial (arg) {
  if (arg === 0) {
    return 1;
  } else {
    return arg * factorial(arg - 1);
  }
}
if (!isNaN(arg)) {
  const res = factorial(arg);
  console.log(res);
} else {
  console.log(1);
}
