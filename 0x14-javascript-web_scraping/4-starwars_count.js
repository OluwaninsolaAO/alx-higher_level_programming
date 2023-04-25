#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit();
}
const id = 18;
const target = `https://swapi-api.alx-tools.com/api/people/${id}/`;

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== '200') {
    process.exit();
  }

  let count = 0;
  const resp = JSON.parse(body);
  const results = resp.results;
  for (const episode of results) {
    if (episode.characters.includes(target)) {
      count++;
    }
  }
  console.log(String(count));
});
