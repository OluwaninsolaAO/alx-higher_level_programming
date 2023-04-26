#!/usr/bin/node

const request = require("request");

if (process.argv.length !== 3) {
  process.exit();
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
    process.exiy();
  }

  const film = JSON.parse(body);

  const characterNames = await Promise.all(
    film.characters.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
            return;
          }

          const character = JSON.parse(body);

          resolve(character.name);
        });
      });
    })
  );

  characterNames.forEach((name) => console.log(name));
});
