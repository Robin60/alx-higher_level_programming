#!/usr/bin/node
// Executes x times a function

exports.callMemoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
