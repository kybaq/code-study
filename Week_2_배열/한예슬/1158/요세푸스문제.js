// 문제링크:https://www.acmicpc.net/problem/1158
// 연결리스트

// 원에서 사람들이 제거되는 순서를 (N,K)-요세푸스 순열이라고 함
// 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있음
// *** 이동한 후에는 그 위치가 현재위치가 됨!!***
// *** mod 연산으로 원형처리 ***
// 인덱스는 k-1 위치.

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split(" ");
const N = Number(input[0]);
const K = Number(input[1]);
const array = Array.from({ length: N }, (_, i) => i + 1);
let idx = 0;
const answer = [];

while (array.length > 0) {
  const currenIdx = (idx + K - 1) % array.length;
  answer.push(array[currenIdx]);
  array.splice(currenIdx, 1);
  idx = currenIdx;
}

console.log(`<${answer.join(", ")}>`);
