#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
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
