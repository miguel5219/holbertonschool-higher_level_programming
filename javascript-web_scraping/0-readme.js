#!/usr/bin/node
const file_ = require('fs');
const file = process.argv[2];
file_.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
