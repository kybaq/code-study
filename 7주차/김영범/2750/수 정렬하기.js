const fs = require("fs");
const filePath = "./input.txt";

const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const length = input.splice(0, 1);

console.log(input.sort().join("\n"));
