// 문제 링크: https://www.acmicpc.net/problem/18258

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath))
  .trim()
  .split("\n")
  .map((el) => el.replace("\r", ""));

input.splice(0, 1);

const queue = [];
const result = [];

let frontIndex = 0;

const actions = (command, value) => {
  // value 는 optional
  const commands = {
    empty: () => {
      return queue.length === frontIndex ? 1 : 0;
    },
    push: (value) => {
      queue.push(value);
    },
    pop: () => {
      return queue.length > frontIndex ? queue[frontIndex++] : -1;
    },
    size: () => {
      return queue.length - frontIndex;
    },
    front: () => {
      return queue.length > frontIndex ? queue[frontIndex] : -1;
    },
    back: () => {
      return queue.length > frontIndex ? queue[queue.length - 1] : -1;
    },
  };

  return commands[command]?.(value);
};

for (const commands of input) {
  const [command, value] = commands.split(" ");

  if (command.includes("push")) {
    actions("push", parseInt(value));
  } else {
    result.push(actions(command, value));
  }
}

console.log(result.join("\n"));
