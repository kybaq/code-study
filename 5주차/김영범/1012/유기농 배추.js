// 문제 링크: https://www.acmicpc.net/problem/1012
// 모든 테스트 케이스가 한 번의 입력으로 들어와서, 각 테이스 케이스 별로 구분하고 bfs 를 실행해서 결과를 출력할 수 있도록 해야함.

const fs = require("fs");
const filePath = "./input.txt";

const inputs = fs.readFileSync(filePath).toString().trim().split("\n");
const numOfTestCases = inputs.splice(0, 1).map(Number);

let index = 0; // inputs 배열에서 테스트 케이스 정보를 가져오기 위함(가로, 세로, 배추 개수 정보)

for (let t = 0; t < numOfTestCases; t++) {
  let [width, height, counts] = inputs[index].split(" ").map(Number); // 테스트 케이스의 크기 정보

  // 각 테스트 케이스 별로, 바로 bfs 실행하기 위해.
  const grid = Array.from({ length: height }, () => new Array(width).fill(0));
  const visited = Array.from({ length: height }, () =>
    new Array(width).fill(false)
  );

  for (let i = index + 1; i <= counts + index; i++) {
    const [coordX, coordY] = inputs[i].split(" ").map(Number);
    grid[coordY][coordX] = 1;
  }

  index += counts + 1;

  // 각 테스트 케이스 별로 bfs 실행
  const dx = [1, 0, -1, 0];
  const dy = [0, 1, 0, -1];
  const queue = []; // 배추가 있는 곳의 위치를 저장하는 큐
  let worms = 0;

  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      if (visited[y][x] || grid[y][x] === 0) continue;
      else {
        visited[y][x] = true;
        queue.push([x, y]);
        worms++;
      }

      while (queue.length) {
        let [curX, curY] = queue.shift();
        // 상하좌우 이동
        for (let k = 0; k < 4; k++) {
          let nx = curX + dx[k];
          let ny = curY + dy[k];

          if (nx < 0 || nx >= width || ny < 0 || ny >= height) continue;
          else if (visited[ny][nx] || grid[ny][nx] === 0) continue;
          else {
            visited[ny][nx] = true;
            queue.push([nx, ny]);
          }
        }
      }
    }
  }
  console.log(worms);
}
