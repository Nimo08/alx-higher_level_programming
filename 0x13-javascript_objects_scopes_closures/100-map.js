#!/usr/bin/node
const dataModule = require('./100-data.js');
const list = dataModule.list;
// val - current element, index - position of current element
const res = list.map((val, index) => val * index);
console.log(list);
console.log(res);
