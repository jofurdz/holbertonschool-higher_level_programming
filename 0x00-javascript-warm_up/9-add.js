#!/usr/bin/node

function add (a, b) {
  return a + b;
}
const myVar = parseInt(process.argv[2]);
const myVar1 = parseInt(process.argv[3]);
console.log(add(myVar, myVar1));
