#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length > 1) {
  console.log('Arguments found');
} else if (argv.length === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
