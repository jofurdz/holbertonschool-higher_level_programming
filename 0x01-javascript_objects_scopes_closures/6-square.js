#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (i) {
    if (i === undefined) {
      i = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      console.log(i.repeat(this.width));
    }
  }
};
