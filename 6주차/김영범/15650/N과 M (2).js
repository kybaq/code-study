// 문제 링크: https://www.acmicpc.net/problem/15650

const fs = require("fs");
const filePath = "./input.txt";

const [n, m] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const array = [];
const isUsed = [];

const backtrack = (length) => {
  if (length === m) {
    return console.log(array.join(" "));
  }

  for (let i = 1; i <= n; i++) {
    if (!isUsed[i]) {
      array[length] = i;
      // 중복을 제거하려면, 직전에 추가된 값보다 작은 수는 배열에 추가하지 못하도록 설정해주면 된다.
      for (let j = 1; j <= i; j++) {
        isUsed[j] = true;
      }
      backtrack(length + 1);
      // 수열 하나를 완성했으니, 다음 수열을 만들기 위해 초기화.
      for (let l = 1; l <= i; l++) {
        isUsed[l] = false;
      }
    }
  }
};

backtrack(array.length);
