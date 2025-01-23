// 문제링크:https://www.acmicpc.net/problem/2164
// 큐

// 주어진 N까지의 수를 나열한 후 홀수번째 값들을 차례대로 지운다.
// 마지막에 1개 남을때까지 반복하면 됨

const fs = require("fs");
const N = Number(fs.readFileSync("/dev/stdin").toString().trim());

let queue = Array.from({ length: N }, (_, i) => i + 1);
let index = 0;

while (queue.length - index > 1) {
  index++; // 맨 앞 카드 버리기 (shift 대신 index 증가)
  queue.push(queue[index]); // 두 번째 카드를 뒤로 이동
  index++; // 다시 index 증가
}

console.log(queue[index]); // 마지막 남은 카드 출력

// let arr = [];

// for (let i = 1; i <= N; i++) {
//   arr.push(i);
// }
// 1. filter 사용
// while (arr.length > 1) {
//   arr = arr.filter((_, index) => index % 2 !== 0);
// }

// 2. queue 사용 -> 시간초과
// while (arr.length > 1) {
//   arr.shift();
//   arr.push(arr.shift());
// }

console.log(arr[0]);
