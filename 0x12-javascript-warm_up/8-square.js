#!/usr/bin/node
let arg = process.argv[2], i = 0, j = 0;
if ((isNaN(arg))) console.log('Missing size');
while ((i++ < arg))
{
  while ((j++ < arg)) process.stdout.write('X');
  j = 0;
  process.stdout.write('\n');
}
