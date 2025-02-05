// 문제 링크: https://www.acmicpc.net/problem/1012

const fs = require("fs");
const filePath = "./input.txt";

const inputs = fs.readFileSync(filePath).toString().trim().split("\n");
const numOfTestCases = inputs[0];

for (let i = 1; i < inputs.length; i++) {
  let input = inputs[i].split(" ").map(Number);

  const [width = 0, height = 0, counts = 0] = input.length > 2 ? input : [];

  console.log(width, height, counts);
}
