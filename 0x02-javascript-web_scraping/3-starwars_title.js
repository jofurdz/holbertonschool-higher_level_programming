#!/usr/bin/node

const request = require('request');
const StarWars = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(StarWars, function (_error, _response, body) {
  const myVar = JSON.parse(body);
  console.log(myVar.title);
});
