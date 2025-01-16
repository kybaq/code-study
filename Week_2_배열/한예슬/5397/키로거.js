// 문제링크: https://www.acmicpc.net/problem/5397
// 연결리스트

// 키로거는 사용자가 키보드 누른 명령을 모두 기록
// 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표
// 길이가 L 인 문자열
// 백스페이스 - / 화살표 < >

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split("\n");
const testCaseNum = Number(input[0]);
const results = [];

for (let t = 1; t <= testCaseNum; t++) {
  const test = input[t];
  const leftStack = [];
  const rightStack = [];

  for (let i = 0; i < test.length; i++) {
    if (test[i] === "<") {
      if (leftStack.length > 0) {
        rightStack.push(leftStack.pop()); // 왼쪽 스택에서 꺼내서 오른쪽으로 이동
      }
    } else if (test[i] === ">") {
      if (rightStack.length > 0) {
        leftStack.push(rightStack.pop()); // 오른쪽 스택에서 꺼내서 왼쪽으로 이동
      }
    } else if (test[i] === "-") {
      if (leftStack.length > 0) {
        leftStack.pop(); // 왼쪽 스택에서 삭제
      }
    } else {
      leftStack.push(test[i]); // 문자 입력 (왼쪽 스택에 추가)
    }
  }

  // `leftStack` + `rightStack.reverse()` 형태로 최종 결과 생성
  results.push(leftStack.join("") + rightStack.reverse().join(""));
}

console.log(results.join("\n"));

// splice 사용 -> 시간초과
// const fs = require("fs");
// const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

// const input = String(fs.readFileSync(filePath)).trim().split("\n");
// const testCaseNum = Number(input[0]);
// const results = [];

// for (let t = 1; t <= testCaseNum; t++) {
//   const test = input[t];
//   let currentIdx = 0;
//   const answer = [];

//   for (let i = 0; i < test.length; i++) {
//     if (test[i] === "<") {
//       if (currentIdx > 0) currentIdx--;
//     } else if (test[i] === ">") {
//       if (currentIdx < answer.length) currentIdx++;
//     } else if (test[i] === "-") {
//       if (currentIdx > 0) {
//         answer.splice(currentIdx - 1, 1);
//         currentIdx--;
//       }
//     } else {
//       answer.splice(currentIdx, 0, test[i]);
//       currentIdx++;
//     }
//   }

//   results.push(answer.join(""));
// }

// console.log(results.join("\n"));
