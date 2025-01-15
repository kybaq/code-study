const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = String(fs.readFileSync(filePath)).trim().split(" ");
const circular = [];

for (let i = 1; i <= input[0]; i++) {
  circular.push(i);
}

let permutation = [];

let index = 0;

while (circular.length !== 0) {
  index = (index + input[1] - 1) % circular.length;
  let temp = circular.splice(index, 1);
  permutation.push(temp);
}

console.log(`<${permutation.join(", ")}>`);
