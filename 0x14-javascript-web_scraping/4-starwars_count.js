#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit();
}
const id = 18;

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    process.exit();
  } else if (response.statusCode !== 200) {
    process.exit();
  }

  let count = 0;
  const resp = JSON.parse(body);
  const results = resp.results;
  for (const episode of results) {
    for (const character of episode.characters) {
      if (character.indexOf(id) !== -1) {
        count++;
      }
    }
  }
  console.log(count);
});
