#!/usr/bin/node

const oldSquare = require('./5-square');

module.exports = class Square extends oldSquare {
  charPrint (c) {
    let sym = 'X';
    let i;

    if (c) {
      sym = c;
    }

    for (i = 0; i < this.height; i++) {
      console.log(sym.repeat(this.width));
    }
  }
};
