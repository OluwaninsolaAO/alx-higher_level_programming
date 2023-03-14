#!/usr/bin/node

exports.esrever = function (list) {
  let i;
  const newList = [];

  for (i = 0; i < list.length; i++) {
    newList[i] = list[list.length - 1 - i];
  }
  return (newList);
};
