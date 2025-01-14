const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split("\n");
const x = Number(input[2]);

const numberArr = input[1].split(" ").map(Number);

let count = 0;

const seenValue = new Set();

for (num of numberArr) {
  const complement = x - num;

  if (seenValue.has(complement)) count++;

  seenValue.add(num);
}

console.log(count);

// const numberStr = input[1].split(" "); // 수열의 원소들
// const numberArr = []; // 수열을 담을 배열

// for (number of numberStr) {
//   numberArr.push(Number(number)); // 원소 추가
// }

// for (let i = 0; i < length; i++) {
//   //   const temp = []; // 조건을 만족하는 쌍을 저장하기 위함
//   //   for (let k = i + 1; k < length; k++) {
//   //     if (numberArr[k] === x - numberArr[i]) {
//   //       temp.push(numberArr[i], numberArr[k]);
//   //       answerArr.push(temp);
//   //       answerArr.push(numberArr[k]);
//   //     }
//   //   }
// }

// console.log(numberArr.length);
