#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], (_err, _res, body) => {
  fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
