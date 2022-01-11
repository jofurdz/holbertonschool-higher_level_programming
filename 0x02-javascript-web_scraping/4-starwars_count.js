#!/usr/bin/node

const request = require('request');
const starWars = process.argv[2];
request(starWars, (_error, _response, body) => {
  let count = 0;
  const myVar = JSON.parse(body).results;
  for (let x = 0; x < myVar.length; x++) {
    for (let i = 0; i < myVar[x].characters.length; i++) {
      if (myVar[i].characters[x].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
