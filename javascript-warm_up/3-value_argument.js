#!/usr/bin/node
const argument = 0;
process.argv.forEach(element => { argv++; });
if (argument === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
