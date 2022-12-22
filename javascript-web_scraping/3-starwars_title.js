#!/usr/bin/node
const request = require('request');
const idMovie = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + idMovie;
request.get(url, (error, response, body) => {
  if (error) console.log(error);
  console.log(JSON.parse(body).tittle);
});
