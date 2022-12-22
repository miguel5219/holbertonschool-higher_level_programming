#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let n = 0; n < this.height; n++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
