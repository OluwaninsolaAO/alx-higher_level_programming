#!/usr/bin/node

let arr = process.argv.slice(2);
arr.sort();
arr = [...new Set(arr)];

if (arr.length <= 1) {
  console.log(0);
} else {
  console.log(arr[arr.length - 2]);
}
