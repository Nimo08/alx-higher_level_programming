#!/usr/bin/node
const dataModule = require('./101-data.js');
const dict = dataModule.dict;
const newDict = {}; // create new dictionary
for (const user in dict) { // loop through original dict
  const key = dict[user];
  if (newDict[key]) { // check if key exists
    newDict[key].push(user); // add user id
  } else {
    newDict[key] = [user]; // create new
  }
}
console.log(newDict);
