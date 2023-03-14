#!/usr/bin/node

const conversion = parseInt(process.argv[2]);

if (!conversion) {
  console.log('Not a number');
} else {
  console.log(`My number: ${conversion}`);
}
