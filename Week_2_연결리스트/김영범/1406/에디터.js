// 문제 링크: https://www.acmicpc.net/problem/1406
// 핵심: 커서의 움직임에 따라 문자열이 추가되는 위치가 달라지는데, 연결리스트 처럼 동작할 수 있는 구조를 떠올려야함. O(N^2) 을 반드시 피해야할 것.

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath))
  .trim()
  .split("\n")
  .map((el) => el.replace("\r", ""));

const initialString = input[0];
const numberofCmds = input[1];

const left = [];
const right = [];

for (const element of initialString) {
  left.push(element);
}

const commands = input.splice(2, numberofCmds);

for (const command of commands) {
  if (command === "L") {
    if (left.length > 0) {
      right.push(left.pop());
    }
  } else if (command === "D") {
    if (right.length > 0) {
      left.push(right.pop());
    }
  } else if (command === "B") {
    left.pop();
  } else {
    left.push(command.split(" ")[1]);
  }
}

console.log(left.join("") + right.reverse().join(""));
