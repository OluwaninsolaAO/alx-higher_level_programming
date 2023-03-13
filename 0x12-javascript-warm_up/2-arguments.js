#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length > 1) {
  console.log('Arguements found');
} else if (argv.length === 1) {
  console.log('Arguement fount');
} else {
  console.log('No argument');
}
