#!/usr/bin/node
const argument = process.argv[2];
const x = parseInt(argument);
const y = (function factorial (x) {
  if (isNaN(x)) {
    return 1;
  } else if (x === 0) {
    return 1;
  } else if (x < 0) {
    return 'does not exist';
  } else {
    return (x * factorial(x - 1));
  }
})(x);
console.log(y);
