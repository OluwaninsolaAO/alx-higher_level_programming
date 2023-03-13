#!/usr/bin/node
import { argv } from 'node:process';

if (argv.length > 3) {
  console.log('Arguements found');
} else if (argv.length === 3) {
  console.log('Arguement fount');
} else {
  console.log('No argument');
}
