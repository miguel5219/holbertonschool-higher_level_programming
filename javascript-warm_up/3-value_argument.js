#!/usr/bin/node
let argument = 0;
process.argv.forEach(element => { argument++; });
if (argument === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
