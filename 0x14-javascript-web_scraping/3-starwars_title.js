#!/usr/bin/node
const request = require('request');
request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (error, response, body) => { error && response.statusCode != 200 ? console.error(error) : console.log(JSON.parse(body).title)});
