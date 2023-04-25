#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  process.exit();
}

const [url, path] = process.argv.slice(2);

request(url).pipe(fs.createWriteStream(path));
