#!/usr/bin/node
const Square5 = require('./5-square.js');
class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X'; // set c to X instead of calling print
    }// use the rectangle width & height instead of size
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect += c;
      }
      console.log(rect);
    }
  }
}
module.exports = Square;
