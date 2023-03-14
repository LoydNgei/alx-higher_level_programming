#!/usr/bin/node

const conversion = parseInt(process.argv[2]);

if (!conversion) {
  console.log('Missing number of occurrences');
}

for (let x = 0; x < conversion; x++) {
  console.log('C is fun');
}
