// 문제 링크: https://www.acmicpc.net/problem/10866

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.replace("\r", ""));

const length = Number(input.splice(0, 1));

const dequeue = [];
const result = [];

let head = Math.floor(length / 2);
let tail = Math.floor(length / 2);

const actions = (command, value) => {
  // value 는 optional
  const commands = {
    push_front: (value) => {
      dequeue[--head] = value;
    },
    push_back: (value) => {
      dequeue[tail++] = value;
    },
    pop_front: () => {
      return head === tail ? -1 : dequeue[head++];
    },
    pop_back: () => {
      return head === tail ? -1 : dequeue[--tail];
    },
    size: () => {
      return tail - head;
    },
    empty: () => {
      return head === tail ? 1 : 0;
    },
    front: () => {
      return head === tail ? -1 : dequeue[head];
    },
    back: () => {
      return head === tail ? -1 : dequeue[tail - 1];
    },
  };

  return commands[command]?.(value);
};

for (const commands of input) {
  const [command, value] = commands.split(" ");

  if (command.includes("push")) {
    actions(command, parseInt(value));
  } else {
    result.push(actions(command));
  }
}

console.log(result.join("\n"));
