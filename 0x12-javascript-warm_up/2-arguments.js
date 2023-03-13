#!/usr/bin/node

if (process.argv.length > 3) {
  console.log('Arguements found');
} else if (process.argv.length === 3) {
  console.log('Arguement fount');
} else {
  console.log('No argument');
}
