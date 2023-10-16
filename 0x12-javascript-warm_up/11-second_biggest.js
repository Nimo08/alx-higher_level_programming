#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else if (process.argv.length > 3) {
  let biggest = -Infinity;
  let secondBiggest = -Infinity;
  const len = process.argv.length;
  for (let i = 0; i < len; i++) {
    if (process.argv[i] > biggest) {
      secondBiggest = biggest;
      biggest = process.argv[i];
    }
  }
  console.log(secondBiggest);
}
