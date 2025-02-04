// 문제 링크: https://www.acmicpc.net/problem/1926

const fs = require("fs");
const filePath = "./input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [height, width] = input.splice(0, 1)[0].split(" ").map(Number);

const array = input.map((row) => row.split(" ").map(Number)); // 그림을 담을 배열
const visited = Array.from({ length: height }, () => new Array(width).fill(0)); // 방문한 위치를 나타내기 위한 배열
const dx = [-1, 0, 1, 0]; // 좌, 우 이동을 위한 배열
const dy = [0, -1, 0, 1]; // 상, 하 이동을 위한 배열열

let numOfPaint = 0; // 그림의 수
let maxArea = 0;

for (let y = 0; y < height; y++) {
  for (let x = 0; x < width; x++) {
    if (array[y][x] === 0 || visited[y][x]) continue; // 값이 0 이거나, 이미 방문한 경우 스킵. 모든 좌표를 순회하는 동안, 방문하지 않았으면서 값이 1인 곳을 찾음.
    ++numOfPaint; // 새로운 그림을 발견한 상황이니, 그림 수 +1
    const paint = [];
    let area = 0; // 영역의 넓이를 저장할 변수
    // const paint = new Map(); // 해당 그림이 이어지는 위치를 저장하기 위한 Map
    // paint.set(`${(y, x)}`, 1); // 해당 그림 위치 추가.
    paint.push({ y, x });
    visited[y][x] = 1;
    while (paint.length) {
      ++area;
      // paint.delete(`${(y, x)}`);
      let { y: curY, x: curX } = paint.shift();
      // 그림이 이어지는 상황에 좌표를 추적하기 위함.
      for (let i = 0; i < 4; i++) {
        // 현재 위치에서 상하좌우 이동 구현
        let nx = curX + dx[i];
        let ny = curY + dy[i];
        if (ny < 0 || ny >= height || nx < 0 || nx >= width) continue; // 상하좌우 이동 시 주어진 좌표 바깥으로 나가는 경우.
        if (array[ny][nx] === 0 || visited[ny][nx]) continue; // 이동한 좌표의 값이 0 이거나, 방문한 경우 스킵.

        // paint.set(`${(ny, nx)}`);
        paint.push({ y: ny, x: nx });
        visited[ny][nx] = 1;
      }
    }
    maxArea = Math.max(maxArea, area);
  }
}

console.log(numOfPaint);
console.log(maxArea);
