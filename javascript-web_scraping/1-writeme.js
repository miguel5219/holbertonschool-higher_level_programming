#!/usr/bin/node
const file_ = require('fs');
const file = process.argv[2];
const writeSecArgument = process.argv[3];
file_.writeFile(file, writeSecArgument, 'utf-8', (err) => {
  if (err) console.log(err);
});
