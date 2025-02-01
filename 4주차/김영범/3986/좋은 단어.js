// 문제 링크: https://www.acmicpc.net/problem/3986
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const length = input.splice(0, 1);

let count = 0;

for (const words of input) {
  let word = words.trim();
  const stack = [];

  for (const char of word) {
    if (stack.includes(char) && char === stack[stack.length - 1]) {
      stack.pop();
    } else {
      stack.push(char);
    }
  }

  if (stack.length === 0) {
    ++count;
  }
}

console.log(count);
