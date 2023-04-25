#!/usr/bin/node
const fileSys = require('fs');

fileSys.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => { err ? console.error(err) : undefined; });
