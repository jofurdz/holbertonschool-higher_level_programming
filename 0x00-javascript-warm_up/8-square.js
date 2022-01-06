#!/usr/bin/node

const myVar = parseInt(process.argv[2]);
let row = '';

if (myVar) {
  for (let x = 0; x < myVar; x++) {
    for (let j = 0; j < myVar; j++) {
      row += 'X';
    }
    console.log(row);
    row = '';
  }
} else {
  console.log('Missing size');
}
