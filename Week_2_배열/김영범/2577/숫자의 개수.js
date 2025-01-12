/*
문제 링크: https://www.acmicpc.net/problem/2577
핵심: 세 숫자 A, B, C 를 곱한 결과값을 문자열로 전환해, 숫자 자체를 배열의 인덱스로 사용한다.
*/

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split("\n").map(Number);

let result = 1;

for (num of input) {
  result *= num;
}

let resultStr = String(result);
let resultArr = [];

for (let i = 0; i < 10; i++) {
  resultArr[i] = 0;
}

for (let l = 0; l < resultStr.length; l++) {
  resultArr[resultStr[l]] += 1;
}

for (num of resultArr) console.log(num);
