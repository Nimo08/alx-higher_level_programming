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
  for (let i = 2; i < len; i++) {
    const num = parseInt(process.argv[i], 10);
    if (!isNaN(num)) {
      if (num > biggest) {
        secondBiggest = biggest;
        biggest = num;
      } else if (num > secondBiggest) {
        secondBiggest = num;
      }
    }
  }
  console.log(secondBiggest);
}
