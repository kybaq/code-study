// 문제 링크: https://www.acmicpc.net/problem/10828

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath))
  .trim()
  .split("\n")
  .map((el) => el.replace("\r", ""));

input.splice(0, 1);

const stack = [];
const result = [];

for (const command of input) {
  if (command.includes("push", 0)) {
    let value = command.split(" ")[1];
    stack.push(value);
  } else if (command === "pop") {
    if (stack.length > 0) result.push(stack.pop());
    else result.push("-1");
  } else if (command === "top") {
    if (stack.length > 0) result.push(stack[stack.length - 1]);
    else result.push("-1");
  } else if (command === "empty") {
    if (stack.length === 0) result.push("1");
    else result.push("0");
  } else if (command === "size") {
    result.push(stack.length);
  }
}

console.log(result.join("\n"));
