#!/usr/bin/node

// computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  const task = JSON.parse(body);
  const dict = {};
  for (let i = 0; i < task.length; i++) {
    if (!dict[task[i].userId]) {
      dict[task[i].userId] = 0;
    }
    if (task[i].completed === true) {
      dict[task[i].userId] += 1;
    }
  }
  console.log(dict);
});
