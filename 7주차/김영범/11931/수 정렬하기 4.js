const fs = require("fs");
const filePath = "./input.txt";

const input = fs.readFileSync(filePath, "utf-8").trim().split("\n").map(Number);

const [length] = input.splice(0, 1);

// for (let i = 0; i < length; i++) {
//   let temp = 0;
//   for (let j = 0; j < length - 1 - i; j++) {
//     if (input[j] < input[j + 1]) {
//       temp = input[j];
//       input[j] = input[j + 1];
//       input[j + 1] = temp;
//     }
//   }
// }

const arr = [];

for (const num of input) {
  arr[length + num] = num;
}

for (let i = arr.length - 1; i > 0; i--) {
  if (arr[i]) console.log(arr[i]);
  else continue;
}
