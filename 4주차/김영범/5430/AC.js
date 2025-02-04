const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.replace("\r", ""));

const testCaseCount = input.splice(0, 1);
const groupSize = 3;

const groupTestCases = (array) => {
  const testCase = [];

  for (let i = 0; i < array.length; i += groupSize) {
    testCase.push(array.slice(i, i + groupSize));
  }

  return testCase;
};

const result = [];
const testCases = groupTestCases(input);

for (const testCase of testCases) {
  const array = testCase[2]
    .slice(1, -1)
    .split(",")
    .filter(Boolean)
    .map((el) => Number(el));

  // left, right 모두 reverse 구현을 위한 방법, 투 포인터 기법이라고 함.
  let left = 0;
  let right = array.length - 1;
  let isReversed = false; // left, right 투 포인터 기반 방향 플래그
  let isError = false; // 길이 0 일 때 "D" 명령 시 오류 처리할 플래그

  for (const command of testCase[0]) {
    if (command === "R") {
      isReversed = !isReversed;
    }
    // else if (array.length > 0) array.shift();
    else if (command === "D") {
      if (left > right) {
        // 같을 경우에는 아직 원소가 하나 남은 상황임.
        // 이때는 이 조건문을 통과할 것이고, 다음에 D 가 한 번 더 남아있다면 에러 처리가 될 것.
        isError = true;
        break;
      }
    }

    isReversed ? --right : ++left; // isReversed 상태가 결정 되고 나면 변화.
  }

  // if (isError) {
  //   result.push("error");
  // } else {
  //   if (left > right) {
  //     // 원소 개수 만큼 "D" 연산을 실시한 상황. 빈 배열일 것.
  //     // "D" 연산을 한 번 이상 더 했다면 위에서 걸려 "error" 가 push.
  //     result.push("[]");
  //   } else {
  //     // right + 1 은 slice 가 마지막 인덱스는 포함하지 않기 때문임.
  //     // +1 안 하면 하나가 빠져버린다.
  //     const subArray = array.slice(left, right + 1);
  //     console.log(subArray);
  //     // result.push(JSON.stringify(isReversed ? subArray.reverse() : subArray));
  //   }
  // }
}

console.log(result.join("\n"));
