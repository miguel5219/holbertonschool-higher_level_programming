#!/usr/bin/node
const form = 'X';
let size = process.argv[2];
size = parseInt(size);
if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  for (let n = 0; n < size; n++) {
    console.log(form.repeat(size));
  }
}
