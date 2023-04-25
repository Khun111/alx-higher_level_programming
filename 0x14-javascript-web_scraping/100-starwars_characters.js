#!/usr/bin/node
const request = require('request');
const castUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(castUrl, (error, response, body) => {
  if (error) console.error(error);
  const data = JSON.parse(body).characters;
  data.forEach((person) => {
    request.get(person, (error, response, body) => {
      if (error) console.error(error);
      console.log(JSON.parse(body).name);
    });
  }
  );
});
