const fs = require("fs");
const filePath = "./input.txt";

const input = fs
  .readFileSync(filePath, "utf-8")
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number));

const [n, m] = input.splice(0, 1)[0];
const [arr1, arr2] = input;
const mergeSortedArr = [];

let idx1 = 0;
let idx2 = 0;

while (idx1 < n && idx2 < m) {
  if (arr1[idx1] <= arr2[idx2]) mergeSortedArr.push(arr1[idx1++]);
  else mergeSortedArr.push(arr2[idx2++]);
}

while (idx1 < n) {
  mergeSortedArr.push(arr1[idx1++]);
}

while (idx2 < m) {
  mergeSortedArr.push(arr2[idx2++]);
}

console.log(mergeSortedArr.join(" "));
