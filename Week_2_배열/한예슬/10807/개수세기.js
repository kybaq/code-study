// 문제링크:https://www.acmicpc.net/problem/10807

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split("\n");

const N = Number(input[0]);
const numbers = input[1].split(" ").map(Number);
const v = Number(input[2]);

// * 반복문 사용
// let answer = 0;
// for (let i = 0; i < numbers.length; i++) {
//   if (v === numbers[i]) {
//     answer++;
//   }
// }

// * filter 사용
const answer = numbers.filter((num) => num === v).length;

console.log(answer);
