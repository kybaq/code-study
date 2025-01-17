// 문제링크:https://www.acmicpc.net/problem/3273
// 배열

// 주어진 수열에 포함되는 수를 순차정렬
// 투 포인터 활용

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath, "utf8").trim().split("\n");

const N = Number(input[0]);
const array = input[1].split(" ").map(Number);
const X = Number(input[2]);

array.sort((a, b) => a - b);

let left = 0;
let right = N - 1;
let answer = 0;

while (left < right) {
  let sum = array[left] + array[right];

  if (sum === X) {
    answer++;
    left++;
    right--;
  } else if (sum < X) {
    left++;
  } else {
    right--;
  }
}

console.log(answer);
