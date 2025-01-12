/*
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42576

접근법: 해시 개념을 이용하지는 못해서, 정렬한 뒤 O(NlogN) 으로 풂.
*/

function solution(participant, completion) {
  var answer = "";

  participant.sort();
  completion.sort();

  for (let i = 0; i < participant.length; i++) {
    if (completion[i] !== participant[i]) {
      answer = participant[i];
      break; // 같은 순서로 정렬을 해두었기에, 다른 게 나온다면 무조건 완주 못한 사람임.
    }
  }
  return answer;
}
