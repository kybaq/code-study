/*
문제 주소: https://school.programmers.co.kr/learn/courses/30/lessons/1845

풀이 접근법
- nums 로 부터 만들어 질 수 있는 조합의 수를 구하는 것이 아님!
- 전체 몇 종류가 있는지 확인 한다음, 그거 다 가져갈 수 있냐 없냐만 확인하면 된다.
*/

function solution(nums) {
  let answer = 0;

  // 내장 Set 을 이용해 간단히 중복 제거. 이를 통해 주어진 폰켓몬 종 수를 구함.
  const cntForSpecies = new Set(nums).size;
  // 그런데, 어차피 가져갈 수 있는 수 제한은 최대 nums / 2 만큼의 수임.
  const cntForMaxSpecies = nums.length / 2;

  // 조금 더 간단한 풀이, answer = Math.min(cntForSpecies, cntForMaxSpecies)
  answer = cntForSpecies <= cntForMaxSpecies ? cntForSpecies : cntForMaxSpecies;

  return answer;
}
