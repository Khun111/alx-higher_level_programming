#!/usr/bin/node
const request = require('request');
request.get('https://swapi-api.alx-tools.com/api/people/18', (error, response, body) => { error || response.statusCode !== 200 ? console.error(error) : console.log(JSON.parse(body).films.length); });
