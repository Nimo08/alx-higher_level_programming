#!/usr/bin/node
exports.esrever = function (list) {
  const array1 = []; // create array to contain reversed list
  for (let i = list.length - 1; i >= 0; i--) {
    const val = list[i]; // assign element in list to val
    array1.push(val); // push values into reversed array
  }
  return array1;
};
