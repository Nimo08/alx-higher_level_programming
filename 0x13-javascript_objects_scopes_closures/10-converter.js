#!/usr/bin/node
exports.converter = function (base) { // sets base for conversion
  return function (num) { // convert a number to the specified base
    return num.toString(base);
  };
};
