// 문제 링크: https://www.acmicpc.net/problem/2630

const fs = require("fs");
const filePath = "./input.txt";

const [n, r, c] = fs
  .readFileSync(filePath, "utf-8")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const recursion = (n, r, c) => {
  if (n === 0) return 0;

  let size = Math.pow(2, n);
  let half = size / 2;

  if (r < half && c < half) {
    // 0번 섹션에 있을 때
    return recursion(n - 1, r, c);
  } else if (r < half && c >= half) {
    // 1번 섹션에 있을 때
    // half 만큼 빼주는 이유는, 함수가 한 번 더 실행되면 전체 배열 크기가 작아지기 때문임.
    // 작아진 크기 만큼 값을 줄여 이동시키는 효과
    // half * half 인 이유는, 한 섹션을 Z 모양으로 순회를 하기 때문에 한 섹션에 들어있는 수 만큼 더해줘야함.
    return half * half + recursion(n - 1, r, c - half);
  } else if (r >= half && c < half) {
    // 2번 섹션에 있을 때
    return half * half * 2 + recursion(n - 1, r - half, c);
  } else {
    // 3번 섹션에 있을 때
    return half * half * 3 + recursion(n - 1, r - half, c - half);
  }
};

console.log(recursion(n, r, c));
