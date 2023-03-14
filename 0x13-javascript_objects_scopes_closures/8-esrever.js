#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length, revArray = [];
  while ((i-- > 0)) revArray.push(list[i]);
  return revArray;
}
