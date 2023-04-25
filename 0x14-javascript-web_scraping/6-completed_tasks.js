#!/usr/bin/node
const request = require('request');
const completedTasks = {};

request.get(process.argv[2], (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error(error);
  }
  const todos = JSON.parse(body);
  todos.forEach((todo) => {
    if (todo.completed) {
      completedTasks[todo.userId] ? completedTasks[todo.userId]++ : completedTasks[todo.userId] = 1;
    }
  });
  console.log(completedTasks);
}
);
