#!/usr/bin/node
let arg = process.argv[2], i = 0, j = 0;
if ((isNaN(arg))) console.log('Missing size');
while ((i++ < arg)) {
  let row = ''
  while ((j++ < arg)) row += ('X');
  j = 0;
  console.log(row);
}
