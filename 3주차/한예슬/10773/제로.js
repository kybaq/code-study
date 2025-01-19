// 문제링크:https://www.acmicpc.net/problem/10773

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const K = Number(input[0]);
let answer = 0;
let stack = [];

for (let i = 1; i <= K; i++) {
  let num = Number(input[i]);

  if (num === 0) {
    if (stack.length > 0) {
      answer -= stack.pop();
    }
  } else {
    stack.push(num);
    answer += num;
  }
}

console.log(answer);
