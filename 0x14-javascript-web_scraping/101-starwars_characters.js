#!/usr/bin/node
const request = require('request');
const castUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(castUrl, (error, response, body) => {
  if (error) console.error(error);
  const data = JSON.parse(body).characters;
  const castMap = new Map();
  data.forEach((person) => {
    request.get(person, (error, response, body) => {
      if (error) console.error(error);
      const name = JSON.parse(body).name;
      castMap.set(person, name);

      if (castMap.size === data.length) {
        data.forEach((cast) => {
          console.log(castMap.get(cast));
        });
      }
    });
  });
});
