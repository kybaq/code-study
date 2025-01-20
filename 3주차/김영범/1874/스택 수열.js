// 문제 링크: https://www.acmicpc.net/problem/1874
// 중첩 반복문이라고 무조건 O(N^2) 이 아니다. 실제 반복 수를 반드시 생각해봐야함.

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const sequenses = String(fs.readFileSync(filePath))
  .trim()
  .split("\n")
  .map((el) => Number(el));

const length = sequenses.splice(0, 1)[0];

const operations = [];
const stack = [];
let current = 1; // 1 - n 까지 한 번만 순회할 수 있도록 만드는 핵심.

for (const target of sequenses) {
  while (current <= target) {
    // !== 를 사용하면, 아직 실제로 추가 안 했는데 stack 에 추가한 것처럼 동작해서 current 가 더 이상 증가하지 않음.
    stack.push(current); // 외부 변수 current 가 있어, 결과적으로는 1 - n 까지만 순회하는 방법임.
    current++;
    operations.push("+");
  }

  if (stack[stack.length - 1] === target) {
    stack.pop();
    operations.push("-");
  } else {
    return console.log("NO"); // 전역 스코프보다 하위에 함수가 없음. return 하게 되면 전역이 종료되어 끝난다.
  }
}

console.log(operations.join("\n"));
