#!/usr/bin/node

const myVar = parseInt(process.argv[2]);

function factorial (myVar) {
  if (isNaN(myVar) || myVar <= 1) {
    return 1;
  } else {
    return myVar * factorial(myVar - 1);
  }
}

console.log(factorial(myVar));
