#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i = 0;
    if ((c === undefined)) c = 'X';
    while ((i++ < this.height)) console.log(c.repeat(this.width));
  }
}
module.exports = Square;
