// 문제 링크: https://www.acmicpc.net/problem/18258

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath))
  .trim()
  .split("\n")
  .map((el) => el.replace("\r", ""));

input.splice(0, 1);

const queue = [];

// for (const command of input) {
//   if (command.includes("push", 0)) {
//     let value = command.split(" ")[1];
//     queue.push(value);
//   } else if (command.includes("pop")) {
//     queue.length > 0 ? console.log(queue.shift()) : console.log(-1);
//   } else if (command.includes("front")) {
//     queue.length > 0 ? console.log(queue[0]) : console.log(-1);
//   } else if (command.includes("back")) {
//     queue.length > 0 ? console.log(queue[queue.length - 1]) : console.log(-1);
//   } else if (command.includes("empty")) {
//     queue.length < 1 ? console.log("0") : console.log("1");
//   } else if (command.includes("size")) {
//     console.log(queue.length);
//   }
// }

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

  if (frontIndex > 10000) {
    queue.splice(0, frontIndex);
    frontIndex = 0;
  }

  if (command.includes("push")) {
    actions("push", parseInt(value));
  } else {
    console.log(actions(command, value));
  }
}
