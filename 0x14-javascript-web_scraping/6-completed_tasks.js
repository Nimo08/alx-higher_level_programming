#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const completeTasks = body.filter(task => task.completed);
  const taskCount = new Map();
  completeTasks.forEach(task => {
    const userId = task.userId;
    taskCount.set(userId, (taskCount.get(userId) || 0) + 1);
  });
  taskCount.forEach((count, userId) => {
    const res = {};
    res[userId] = count;
    console.log(res);
  });
});
