#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  process.exit();
}
const [path, data] = process.argv.slice(2);

fs.writeFile(path, data, (error) => {
  if (error) {
    console.log(error);
  }
});
