// 문제 링크: https://www.acmicpc.net/problem/10773
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split("\n").map(Number);

input.splice(0, 1);

const arr = [];

let result = 0;

for (const money of input) {
  if (money === 0) arr.pop();
  else arr.push(money);
}

if (arr.length !== 0) {
  for (const money of arr) result += money;
}

console.log(result);
