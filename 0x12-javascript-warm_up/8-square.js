#!/usr/bin/node

const count = parseInt(process.argv[2]);
const symbol = 'X';
let square = '';
let i;

if (!count) {
  console.log('Missing size');
}

for (i = 0; i < count; i++) {
  square = square + symbol;
}

for (i = 0; i < count; i++) {
  console.log(square);
}
