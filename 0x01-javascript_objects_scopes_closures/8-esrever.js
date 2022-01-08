#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];
  for (let x = list.length - 1; x >= 0; x--) {
    arr.push(list[x]);
  }
  return arr;
};
