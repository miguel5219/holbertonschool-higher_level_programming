#!/usr/bin/node
const request = require('request');
const urlApi = process.argv[2];
request(urlApi, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const file = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (file[task.userId]) {
        file[task.userId]++;
      } else {
        file[task.userId] = 1;
      }
    }
  }
  console.log(file);
});
