#!/usr/bin/node

const request = require('request');

request(process.argv[2], (_error, response) => {
  if (_error) {
    console.log(_error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
