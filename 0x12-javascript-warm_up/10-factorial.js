#!/usr/bin/node
let arg = process.argv[2];
function fact(n)
{
	if (!n || n == 1)
		return (1);
	return (n * fact(n-1));
}
console.log(fact(arg));
