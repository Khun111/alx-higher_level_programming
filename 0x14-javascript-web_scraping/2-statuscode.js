#!/usr/bin/node
request = require('request')
request.get(process.argv[2], (error, response, body) => console.log(`code: ${response.statusCode}`));