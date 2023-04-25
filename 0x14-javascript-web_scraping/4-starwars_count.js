#!/usr/bin/node
const request = require('request');
const hisId = '18';
let count = 0;
request.get(process.argv[2], (error, response, body) => {
  if (error) console.error(error);
  const data = JSON.parse(body).results;
  data.forEach((movies) => {
    movies.characters.forEach((movie) => {
      if (movie.includes(hisId)) count++;
    });
  }
  );
  console.log(count);
});
