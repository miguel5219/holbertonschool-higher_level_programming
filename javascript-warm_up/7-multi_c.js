#!/usr/bin/node
let myVar = process.argv[2];
myVar = parseInt(myVar);
if (isNaN(myVar)) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
}
