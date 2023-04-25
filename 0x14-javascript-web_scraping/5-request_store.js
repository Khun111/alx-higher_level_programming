#!/usr/bin/node
const request = require('request');
const fileSys = require('fs');

request.get(process.argv[2], (error, response, body) => {
  if (error && response.statusCode !== 200) {
    console.error(error);
  } else {
    fileSys.writeFile(process.argv[3], body, 'utf-8', (err) => { err ? console.error(err) : undefined; });
  }
});
