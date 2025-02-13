// 문제 링크: https://www.acmicpc.net/problem/10026

const fs = require("fs");
const filePath = "./input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(input.shift());

const queue = [];
const visited = Array.from({ length: N }, () => new Array(N).fill(false));

const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];

let current = null; // 현재 확인한 색
let last = null; // 마지막에 확인한 색
let area = 0; // 영역 수
let area_cb = 0; // 적록색맹일 경우 영역 수

for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    current = input[y][x]; // 현재 색깔

    if (visited[y][x] || current === last) continue; // 같은 색일 경우 or 이미 방문했으면 그냥 넘어감.
    else {
        // 직전에 방문하지 않았으면서, 직전에 확인한 값과 다른 경우
      visited[y][x] = true;
      queue.push([x, y]);
    }

    while (queue.length) {
      const [curX, curY] = queue.shift();

      for (let i = 0; i < 4; i++) {
        const nx = curX + dx[i];
        const ny = curY + dy[i];

        if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
        else if (visited[ny][nx] || current === last) continue;
        else {
          console.log(ny, nx, current, last); 
          // 범위 안의 값이면서, 방문하지도 않았고, 직전에 방문한 곳의 색과도 다른 경우
          visited[ny][nx] = true; // 방문 여부 갱신
          last = input[curY][curX]; // 직전에 방문한 값 갱신
          current = input[ny][nx]; // 현재 값 갱신
          queue.push([nx, ny]);

          // 적록색맹일 경우 계산을 다르게 하기 위한 조건문
          if (visited[curY][curX] || current === last) continue;
          else {
            if((current === "R" && last === "G") ||  (current === "G" && last === "R")) area++;
            else {
            area++;
            area_cb++;
            }
          }
        }
      }
    }
  }
}

console.log(area, area_cb); 