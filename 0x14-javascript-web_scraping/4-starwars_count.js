#!/usr/bin/node
const request = require('request');
const castUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;
request.get(process.argv[2], (error, response, body) => {
  if (error) console.error(error);
  const data = JSON.parse(body).results;
  data.forEach((movie) => {
    if (movie.characters.includes(castUrl)) count++;
  }
  );
  console.log(count);
});
