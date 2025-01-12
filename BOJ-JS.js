/* 
출처: https://oesnuj.tistory.com/entry/Javascript-백준-nodejs로-풀-때-케이스-별-입력-처리하는-방법 [비트로 그리는 성장일기:티스토리]
https://valueengine.tistory.com/2

위 블로그를 참고해 본 템플릿을 만들게 되었습니다.

## 목적

node.js 를 이용하지 않으면, 백준 환경에서는 JS 로 문제 풀이가 불가능합니다.
node.js 는 fs 모듈을 통해 파일 입/출력이 가능하기에, 이를 활용해 백준 같은 표준 리눅스 환경에서도 문제 풀이가 가능하도록 만든 템플릿입니다.

## 입력 처리 방식 예제

아래는 각 테스트 케이스 별 입력 처리 방식 예시입니다.
예시를 참고해서 문제마다 적절하게 입력 값을 처리해줘야합니다.

1. 입력 데이터가 한 개일 경우 TODO -> const input = fs.readFileSync(filePath).toString().trim();
2. 입력 데이터가 한 줄에 여러 개 들어올 경우 TODO -> const input = fs.readFileSync(filePath).toString().trim().split(' ');
3. 입력 데이터가 여러 줄에 걸쳐 들어올 경우 TODO -> const input = fs.readFileSync(filePath).toString().trim().split('\n');

이외에도 다양한 예시가 있으므로, 사용이 어렵다면 출처에 기재한 블로그들을 참고하시길 바랍니다.

## 참고 사항

NOTE: 본 템플릿을 통해, 문제마다 적절하게 변형해야 풀이가 가능합니다.
VSCode 로 코드르 실행할 경우, `.js` 파일과 같은 경로에 `input.txt` 를 생성해 테스트 케이스를 넣어두면 됩니다.

*/
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
