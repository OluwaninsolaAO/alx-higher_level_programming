#!/usr/bin/node

let i;

for (i = 0; process.argv[i]; i++) {
  continue;
}

console.log(i === 2 ? 'No argument' : process.argv[2]);
