const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim();
const numArr = Array(10).fill(0); // 0 - 9 사이의 숫자가 등장하는 횟수를 세기 위해, 미리 값을 채워둠. 추후 연산을 편하게 할 수 있다.

for (number of input) {
  if (number === "6" || number === "9") {
    numArr[6] <= numArr[9] ? (numArr[6] += 1) : (numArr[9] += 1); // 6과 9는 같은 숫자로 보면 되니까, 번호판을 최소로 사용하는 방법.
  } else {
    numArr[number] += 1;
  }
}

let answer = 0;

// 몇 개의 번호판이 필요한지 확인
for (count of numArr) {
  answer = answer <= count ? count : answer;
}

console.log(answer);
