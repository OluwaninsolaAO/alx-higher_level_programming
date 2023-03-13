#!/usr/bin/node

const num = parseInt(process.argv.slice(2));

if (num) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
