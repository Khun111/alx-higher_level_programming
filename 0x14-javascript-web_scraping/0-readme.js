#!/usr/bin/node
const fileSys = require('fs');

fileSys.readFile(process.argv[2], 'utf-8', (err, data) => { err ? console.error(err) : console.log(data); });
