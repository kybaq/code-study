// 문제 링크: https://www.acmicpc.net/problem/1926

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [height, width] = input.splice(0, 1)[0].split(" ").map(Number);

const array = []; // 그림을 담을 배열
const visited = []; // 방문한 위치를 나타내기 위한 배열
const dx = [1, 0, -1, 0]; // 좌, 우 이동을 위한 배열
const dy = [0, 1, 0, -1]; // 상, 하 이동을 위한 배열열

let numOfPaint = 0; // 그림의 수

for (const rows of input) {
  const row = rows.split(" ").map(Number);
  const rowArr = [];

  for (const col of row) {
    rowArr.push(col);
  }

  array.push(rowArr);
}

for (let h = 0; h < height; h++) {
  for (let w = 0; w < width; w++) {
    if (area[h][w] === 0 || visited[h][w]) continue; // 값이 0 이거나, 이미 방문한 경우 스킵. 모든 좌표를 순회하며 방문하지 않았으면서 값이 1인 곳을 찾음.
    let area = 0; // 영역의 넓이를 저장할 변수
    const paint = []; // 해당 그림이 이어지는 위치를 저장하기 위한 배열
    ++numOfPaint; // 새로운 그림을 발견한 상황이니, 그림 수 +1
    paint[h][w] = 1;
    while (!paint.length) {
      // 그림이 이어지는 상황에 좌표를 추적하기 위함.
    }
  }
}
