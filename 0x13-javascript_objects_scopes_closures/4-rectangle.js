#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 || h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rect = ''; // building rows
      for (let j = 0; j < this.width; j++) {
        rect += 'X'; // appending the X to the rows
      }
      console.log(rect); // print the shape inside the outer for loop
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () { // individually multiply width and height by 2
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
