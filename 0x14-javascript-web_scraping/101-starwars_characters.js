#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit();
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const characters = new Map(Object.entries(JSON.parse(body).characters));
    for (const data of characters.values()) {
      request(data, function (error, response, body) {
        if (error) {
          console.log(error);
        } else if (response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    }
  }
});
