#!/usr/bin/node
class Square extends require('./5-square') {
  charPrint (c) {
    let i = 0;
    if ((c === undefined)) this.print();
    else while ((i++ < this.height)) console.log(c.repeat(this.width));
  }
}
module.exports = Square;
