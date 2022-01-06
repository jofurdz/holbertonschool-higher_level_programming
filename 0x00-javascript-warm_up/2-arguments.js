#!/usr/bin/node

const myVar = 'No argument';
const myVar1 = 'Argument found';
const myVar2 = 'Arguments found';

if (process.argv.length > 3) {
  console.log(myVar2);
} else if (process.argv.length === 3) {
  console.log(myVar1);
} else {
  console.log(myVar);
}
