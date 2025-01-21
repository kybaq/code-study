// 문제 링크: https://www.acmicpc.net/problem/2493

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split("\n");

const length = Number(input[0]);

const stack = input[1].split(" ").map(Number);

const position = [];

for (let i = 0; i < length; i++) {
  let top = stack.pop();
  let cursor = stack.length - 1;

  while (top > stack[cursor]) {
    if (cursor > 0) {
      cursor--;
    }
  }
  position.push(cursor + 1);
}

console.log(position.reverse().join(" "));
