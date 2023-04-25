#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit();
}

request(process.argv[2], function (error, response, body) {
  console.log(`code: ${response.statusCode}`);
});
