#!/usr/bin/node

// computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  const tasks = JSON.parse(body);
  const dict = {};
  for (let i = 0; i < tasks.length; i++) {
    if (!dict[tasks[i].userId]) {
      dict[tasks[i].userId] = 0;
    }
    if (tasks[i].completed === true) {
      dict[tasks[i].userId] += 1;
    }
  }
  console.log(dict);
});
