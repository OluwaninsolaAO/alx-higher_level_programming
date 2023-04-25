#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit();
}

const target = 'https://swapi-api.alx-tools.com/api/people/18/';

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }

  let count = 0;
  const resp = JSON.parse(body);
  const results = resp.results;
  for (const episode of results) {
    if (episode.characters.includes(target)) {
      count++;
    }
  }
  console.log(count);
});
