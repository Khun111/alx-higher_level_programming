#!/usr/bin/node
const request = require('request');
const fileSys = require('fs');

request.get(process.argv[2], (error, response, body) => { error && response.statusCode !== 200 ? console.error(error) : data = JSON.parse(body); });

fileSys.writeFile(process.argv[3], data, 'utf-8', (err) => { err ? console.error(err) : console.log('Successful'); });
