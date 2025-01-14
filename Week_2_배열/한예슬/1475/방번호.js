// 문제링크:https://www.acmicpc.net/problem/1475
// 배열

// 필요한 세트의 개수의 최솟값구하기 (9,6 은 뒤집이서 이용 가능)
// 한 세트에 0-9 까지 하나씩 있음
// 9와 6이 2개까지는 하나의 세트로 활용할수있음. -> 나누고 나머지 올림 사용해야할듯
// 나머지 숫자들은 갯수만큼 세트가 필요함

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim();
let answer = 0;
const count = new Array(10).fill(0);

for (let i = 0; i < input.length; i++) {
  const num = Number(input[i]);
  count[num]++;
}

count[6] = Math.ceil((count[6] + count[9]) / 2); // 9와 6의 수를 6으로 합쳤기 때문에 9는 0 으로 초기화 해줘야함
count[9] = 0;

answer = Math.max(...count);

console.log("answer", answer);
