#!/usr/bin/node

// Print the movies with "Wedge Antiles"

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  const data = JSON.parse(body);
  let total = 0;
  for (let i = 0; i < data.results.length; i++) {
    const character = data.results[i].characters;
    for (let j = 0; j < character.length; j++) {
      if (character[j].includes('18')) {
        total = total + 1;
      }
    }
  }
  console.log(total);
});
