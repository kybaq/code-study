// 문제:

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

// const input = fs.readFileSync(filePath).toString().trim().split("\n");

// const [length, wannaPickCount] = input[0].split(" ").map(Number);
// const pickableIndex = input[1].split(" ").map(Number);

// const popped = [];

// let count = 0;
// let head = 0;
// let tail = length;

// const right = () => {
//   --head;
//   ++tail;

//   return;
// };
// const left = () => {
//   ++head % length;
//   ++tail % length;
// };

// while (popped.length !== pickableIndex.length) {
//   let target = pickableIndex[popped.length];
//   console.log(target, head, tail);
//   if (head + 1 === target) {
//     popped.push(head);
//     ++head;
//   } else {
//     ++count;
//     Math.abs(target - head) < Math.abs(target - tail) ? left() : right();
//   }
// }

// console.log(count);

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [n, m] = input[0].split(" ").map(Number); // n: 큐의 크기, m: 뽑아낼 원소의 개수
const targets = input[1].split(" ").map(Number); // 뽑아낼 원소의 위치 배열

// 초기 큐를 생성 (1부터 n까지)
let queue = Array.from({ length: n }, (_, i) => i + 1);
let totalMoves = 0;

for (const target of targets) {
  const targetIndex = queue.indexOf(target); // 현재 큐에서 target의 인덱스 계산
  const leftMoves = targetIndex; // 왼쪽으로 이동하는 횟수
  const rightMoves = queue.length - targetIndex; // 오른쪽으로 이동하는 횟수

  // 최적의 이동 방향을 선택
  if (leftMoves <= rightMoves) {
    // 왼쪽으로 이동
    totalMoves += leftMoves;
    queue = [...queue.slice(targetIndex + 1), ...queue.slice(0, targetIndex)];
  } else {
    // 오른쪽으로 이동
    totalMoves += rightMoves;
    queue = [...queue.slice(targetIndex + 1), ...queue.slice(0, targetIndex)];
  }
}

console.log(totalMoves);
