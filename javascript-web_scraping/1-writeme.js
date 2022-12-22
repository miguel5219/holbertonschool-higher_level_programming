#!/usr/bin/node
const file_ = require('fs');
const file = process.argv[2];
const write_Sec_argument = process.argv[3];
file_.writeFile(file, write_Sec_argument, 'utf-8', (err) => {
  if (err) console.log(err);
});
