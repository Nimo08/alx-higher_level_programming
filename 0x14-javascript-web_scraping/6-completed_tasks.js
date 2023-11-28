#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const completeTasksUser = {};
  const completeTasks = body.filter(task => task.completed);
  completeTasks.forEach(task => {
    const userId = task.userId;
    completeTasksUser[userId] = (completeTasksUser[userId] || 0) + 1;
  });
  Object.keys(completeTasksUser).forEach(userId => {
    console.log(`${userId}: ${completeTasksUser[userId]}`);
  });
});
