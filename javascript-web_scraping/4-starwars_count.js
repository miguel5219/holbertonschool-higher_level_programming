#!/usr/bin/node
const request = require('request');
const urlApi = process.argv[2];
request(urlApi, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let x = 0;
  for (const result of JSON.parse(body).result) {
    for (const Wedge of result.characters) {
      if (Wedge.includes(18)) {
        x++;
      }
    }
  }
  console.log(x);
});
