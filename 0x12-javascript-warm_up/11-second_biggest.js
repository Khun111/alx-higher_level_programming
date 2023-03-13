#!/usr/bin/node
let arr = process.argv.slice(2);

if (process.argv.length <= 3) console.log(0);
else
{
	const sortArr = arr.sort((a, b) => b - a)
	console.log(sortArr[1]);
}
