#!/usr/bin/node
const argument = process.argv;
const argument1 = parseInt(argument[2]);
const argument2 = parseInt(argument[3]);
function add (argument1, argument2) {
  return argument1 + argument2;
}
console.log(add(argument1, argument2));
