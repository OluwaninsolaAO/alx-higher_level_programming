#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit();
}

const api = 'https://swapi-api.alx-tools.com/api/films/';

request(api + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
