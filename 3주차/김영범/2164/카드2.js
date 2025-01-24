// 문제 링크: https://www.acmicpc.net/problem/2164

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(filePath).toString().trim();

const queue = [];

for (let i = 1; i <= input; i++) {
  queue.push(i);
}

let frontIndex = 0;

for (let l = 0; l < input; l++) {
  frontIndex++;
  queue.push(queue[frontIndex]);
  frontIndex++;
  console.log(queue[frontIndex]);
}
