#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = -1, count = 0;
  while ((i++ < list.length))
  {
    if ((list[i] === searchElement)) count++;
  }
  return count;
}
