// 문제 링크: https://www.acmicpc.net/problem/15649

const fs = require("fs");
const filePath = "./input.txt";

const array = []; // 수열을 담을 배열
const isUsed = []; // 상태 트리를 구현하기 위한 배열, Boolean

// N: 자연수의 범위위
// M: 수열의 길이
const [N, M] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const backTrack = (k) => {
  if (k === M) {
    // k 번 실행되어, 길이 M 만큼의 수열 하나를 완성한 경우
    let number = [];

    for (let i = 0; i < M; i++) {
      number.push(array[i]);
    }

    return console.log(number.join(" ")); // 수열 출력
  }

  // 1 부터 N 까지 자연수 범위
  for (let l = 1; l <= N; l++) {
    if (!isUsed[l]) {
      // 아직 수열에 포함되지 않은 경우
      array[k] = l;
      isUsed[l] = true;
      backTrack(k + 1); // 다음 수를 찾기 위해 한 번 더 실행.

      isUsed[l] = false; // 수열이 완성되어 출력된 이후의 상황.
      // 초기화를 하지 않게 된다면, [1, 2, 3] 같은 수열을 완성하고 나면 이후 [1, 3, 2] 같은 다른 수열은 만들 수가 없게 됨.
      // 하나의 수열을 완성하게 되면 다음 수열에서 쓰기 위해 초기화해준다.
      // 어차피 이렇게 초기화 한 뒤, 바로 다음 수로 넘어가기 때문에 무한 반복이 걸리게되는 일은 없음.
    }
  }
};

backTrack(0);
