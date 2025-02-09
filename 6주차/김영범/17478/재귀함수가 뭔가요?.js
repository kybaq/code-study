// 문제 링크: https://www.acmicpc.net/problem/17478

const fs = require("fs");
const filePath = "./input.txt";

const N = Number(fs.readFileSync(filePath).toString().trim());

let count = 0;

const recursion = (N) => {
  ++count;

  let dash = "____".repeat(count);

  // 메모리 초과가 발생하기 딱 좋은 방법.
  // 함수를 매번 호출할 때 마다, dash 를 계속 더해주는 방식이니 길이가 길어지면서 dash 변수의 크기가 계속 커지게 됨.
  // 반복 횟수만 저장해뒀다가, repeat 같은 내장함수로 그때 그때만 늘려주는 방식을 쓰는게 좋다.
  // for (let i = 1; i < count; i++) {
  // dash += dash;
  // }

  if (N === 1) {
    return `${dash}"재귀함수가 뭔가요?"
${dash}"재귀함수는 자기 자신을 호출하는 함수라네"
${dash}라고 답변하였지.`;
  }

  return `${dash}"재귀함수가 뭔가요?"
${dash}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
${dash}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
${dash}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
${recursion(N - 1)}
${dash}라고 답변하였지.`;
};

console.log(`어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
${recursion(N)}
라고 답변하였지.`);
