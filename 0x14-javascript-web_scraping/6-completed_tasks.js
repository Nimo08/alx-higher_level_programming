#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const completeTasks = body.reduce((count, task) => {
    if (task.completed) {
      const userId = task.userId;
      count[userId] = (count[userId] || 0) + 1;
    }
    return count;
  }, {});
  console.log(completeTasks);
});
