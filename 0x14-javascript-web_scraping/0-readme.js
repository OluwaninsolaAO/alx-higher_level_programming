#!/usr/bin/node

if (process.argv.length !== 3) {
  process.exit();
}

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    process.exit();
  }
  console.log(data);
});
