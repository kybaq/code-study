// 문제링크:https://www.acmicpc.net/problem/1021
// 덱

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split("\n");
const [N, M] = input[0].split(" ").map(Number);
const targets = input[1].split(" ").map(Number);

let deque = Array.from({ length: N }, (_, i) => i + 1);
let operationCount = 0;

for (let target of targets) {
  let idx = deque.indexOf(target);
  let leftMoves = idx;
  let rightMoves = deque.length - idx;

  if (leftMoves <= rightMoves) {
    while (deque[0] !== target) {
      deque.push(deque.shift());
      operationCount++;
    }
  } else {
    while (deque[0] !== target) {
      deque.unshift(deque.pop());
      operationCount++;
    }
  }
  deque.shift();
}

console.log(operationCount);
