#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  let i;

  for (i = 0; list[i]; i++) {
    if (list[i] === searchElement) {
      num++;
    }
  }
  return (num);
};
