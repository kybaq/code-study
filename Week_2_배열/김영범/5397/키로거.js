// 문제 링크: https://www.acmicpc.net/problem/5397

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split("\n");

input.shift();

for (password of input) {
  const left = [];
  const right = [];

  for (const char of password) {
    if (char === "<") {
      if (left.length > 0) right.push(left.pop());
    } else if (char === ">") {
      if (right.length > 0) left.push(right.pop());
    } else if (char === "-") {
      left.pop();
    } else {
      left.push(char);
    }
  }

  //   for (letter of password) {
  //     switch (letter) {
  //       case "<":
  //         if (left.length > 0) {
  //           const temp = left.pop();
  //           right.push(temp);
  //         }
  //         break;

  //       case ">":
  //         if (right.length > 0) {
  //           const temp = right.shift();
  //           left.push(temp);
  //         }
  //         break;

  //       case "-":
  //         left.pop();
  //         break;

  //       default:
  //         left.push(letter);
  //         break;
  //     }
  //   }

  console.log(left.join("") + right.reverse().join(""));
}

// const fs = require("fs");
// const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

// const input = String(fs.readFileSync(filePath)).trim().split("\r\n");
// input.splice(0, 1);

// const robbedPassword = [];

// for (password of input) {
//   let cursor = 0;
//   const loggedPassword = new Map();

//   for (letter of password) {
//     // console.log(letter);
//     switch (letter) {
//       case "<":
//         cursor = cursor > 0 ? (cursor -= 1) : cursor;
//         break;

//       case ">":
//         cursor = cursor >= loggedPassword.size ? cursor : (cursor += 1);
//         break;

//       case "-":
//         if (loggedPassword.size > 0) {
//           console.log("1: ", loggedPassword);
//           loggedPassword.delete(cursor);
//           console.log("2: ", loggedPassword);
//           cursor -= 1;
//         }
//         break;

//       default:
//         if (loggedPassword.has(cursor)) {
//           const temp = loggedPassword.get(cursor);
//           loggedPassword.set(cursor, letter);
//           // 여기서 결국 다 옮기면 O(N) 인데 어떻게 할지?

//           cursor += 1;
//         } else {
//           loggedPassword.set(cursor, letter);
//         }
//         cursor += 1;
//         break;
//     }
//   }
//   robbedPassword.push(loggedPassword);
// }

// console.log(robbedPassword);
