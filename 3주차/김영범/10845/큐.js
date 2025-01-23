// 문제 링크: https://www.acmicpc.net/problem/10845

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath))
  .trim()
  .split("\n")
  .map((el) => el.replace("\r", ""));

input.splice(0, 1);

const queue = [];

for (const command of input) {
  if (command.includes("push", 0)) {
    let value = command.split(" ")[1];
    queue.push(value);
  } else if (command === "pop") {
    if (queue.length > 0) console.log(queue.shift());
    else console.log("-1");
  } else if (command === "front") {
    if (queue.length > 0) console.log(queue[0]);
    else console.log("-1");
  } else if (command === "back") {
    if (queue.length > 0) console.log(queue[queue.length - 1]);
    else console.log("-1");
  } else if (command === "empty") {
    if (queue.length === 0) console.log("1");
    else console.log("0");
  } else if (command === "size") {
    console.log(queue.length);
  }
}
