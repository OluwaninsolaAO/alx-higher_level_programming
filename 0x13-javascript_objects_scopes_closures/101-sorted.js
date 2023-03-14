#!/usr/bin/node

const dict = require('./101-data').dict;
const obj = {};

for (const key in dict) {
  if (dict[key] in obj) {
    obj[dict[key]].push(key);
  } else {
    obj[dict[key]] = [key];
  }
}

console.log(obj);
