#!/usr/bin/node

const myVar = 'No argument';

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log(myVar);
}
