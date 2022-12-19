#!/usr/bin/node
let myvar = process.argv[2];
myvar = parseInt(myvar);
if (isNaN(myvar)) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = 0; i < myvar; i++) {
    console.log('C is fun');
  }
}
