// 문제링크:https://www.acmicpc.net/problem/2577
// 배열

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split("\n");
const multiplication = Number(input[0]) * Number(input[1]) * Number(input[2]);
const multiplicationArray = String(multiplication).split("").map(Number);
const count = new Array(10).fill(0);

for (let i = 0; i < multiplicationArray.length; i++) {
  const num = multiplicationArray[i];
  count[num]++;
}

for (let i = 0; i < count.length; i++) {
  console.log(count[i]);
}
