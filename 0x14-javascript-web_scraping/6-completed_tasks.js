#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit();
}

const url = process.argv[2];

request(url, function (error, response, body) {
  const result = {};

  if (error) {
    process.exit();
  } else {
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (result[todo.userId] === undefined) {
        result[todo.userId] = 0;
      }
      if (todo.completed) {
        result[todo.userId] += 1;
      }
    }

    console.log(result);
  }
});
