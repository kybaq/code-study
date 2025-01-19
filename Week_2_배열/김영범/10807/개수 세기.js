// 문제 링크: https://www.acmicpc.net/problem/10807

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split("\n");

const arr = input[1].split(" ").map(Number);
const target = Number(input[2]);

let count = 0;

for (const num of arr) {
  if (num === target) count++;
}

console.log(count);
