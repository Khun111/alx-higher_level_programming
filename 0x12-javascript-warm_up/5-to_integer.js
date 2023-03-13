#!/usr/bin/node
import { argv } from 'node:process';
if (Number(argv[2]))
	console.log('My number: ' + Math.floor(argv[2]));
else
	console.log('Not a number')
