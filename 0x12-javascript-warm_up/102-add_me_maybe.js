#!/usr/bin/node
// executes x times a function.

exports.addMemaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
