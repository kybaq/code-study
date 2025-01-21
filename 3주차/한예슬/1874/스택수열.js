// 문제링크:https://www.acmicpc.net/problem/1874

// push -> 오름차순
// 어떤 순서로 push, pop 연산을 수행해야 하는지 알아낼 수 있다.
// 둘째줄부터 수열을 이루는 정수가 주어짐. 같은 정수가 두번나오는 일은 없음
// sequence[] 의 index 0 의 값만큼 + 해주고 - 1번은 필수.
// 현재 숫자가 스택의 top보다 크면 push(+) 후 pop(-)
// 작으면 바로 pop(-) 수행
// pop한 값이 목표 숫자가 아니면 "NO" 출력
// 연산을 배열에 저장 후 한 번에 출력

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split("\n");
const N = Number(input[0]);
const sequence = input.slice(1).map(Number);
let stack = [];
let answer = [];
let current = 1; // 현재 push할 숫자 (1부터 시작)

for (const i of sequence) {
  while (current <= i) {
    // i가 나올 때까지 push
    stack.push(current);
    answer.push("+");
    current++; // 다음 숫자로 증가
  }

  if (stack[stack.length - 1] === i) {
    stack.pop();
    answer.push("-");
  } else {
    console.log("NO");
    return;
  }
}

console.log(answer.join("\n"));
