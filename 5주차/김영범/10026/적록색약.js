// 문제 링크: https://www.acmicpc.net/problem/10026

const fs = require("fs");
const filePath = "./input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = input[0];
const queue = [];
const visited = Array.from({ length: N }, () => new Array(N).fill(false));

const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];

let last = ; // 마지막에 확인한 색, 여러 개인 경우는?
let area = 0; // 영역 수
let area_cb = 0; // 적록색맹일 경우 영역 수

for (let y = 1; y <= N; y++) {
  for (let x = 1; x <= N; x++) {
    const current = input[y][x]; // 현재 색깔
    last = last ? last : current; // 직전에 확인한 색이 없으면, 현재 색으로 지정.

    if (current === last || visited[y][x]) continue; // 같은 색일 경우 or 이미 방문했으면 그냥 넘어감.
    else {
        // 직전에 방문하지 않았으면서, 직전에 확인한 값과 다른 경우우
      queue.push([x, y]);
      // current =
    }

    while (queue.length) {
      const [curX, curY] = queue.shift();

      for (let i = 0; i < 4; i++) {
        const nx = curX + dx[i];
        const ny = curY + dy[i];

        if (nx < 0 || nx > N || ny < 0 || ny > N) continue;
        else if (current === last || visited[ny][nx]) continue;
        else {
            // 범위 안의 값이면서, 방문하지도 않았고, 직전에 발견한 새로운 값과도 다른 경우우
        }
      }
    }
  }
}
