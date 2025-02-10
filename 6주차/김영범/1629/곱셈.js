// 문제 링크: https://www.acmicpc.net/problem/1629

const fs = require("fs");
const filePath = "./input.txt";

const [A, B, C] = fs
  .readFileSync(filePath, "utf-8")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let count = 0;

const recursion = (A, B, C) => {
  if (B === 0) {
    return Math.pow(A, count) % C;
  }

  ++count;

  return recursion(A, B - 1, C);
};

console.log(recursion(A, B, C));
