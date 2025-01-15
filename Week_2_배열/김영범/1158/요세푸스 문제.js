const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split(" ");

const length = input[0];
const removeNumber = input[1];

const circular = [];

for (let i = 1; i <= length; i++) {
  circular.push(i);
}

const permutation = [];

let index = 0;

while (circular.length !== 0) {
  index = (index + removeNumber - 1) % circular.length;
  let temp = circular.splice(index, 1);
  permutation.push(temp);
}

console.log(permutation);
