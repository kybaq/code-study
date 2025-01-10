function solution(participant, completion) {
  let answer = "";

  const mapForParticipant = new Map();
  //   const mapForCompletion = new Map();

  for (name of participant) {
    mapForParticipant.set(name, (mapForParticipant.get(name) || 0) + 1);
  }

  for (name of completion) {
    mapForParticipant.set(name, mapForParticipant.get(name) - 1);
  }

  for ([name, count] of mapForParticipant) {
    if (count > 0) answer = name;
  }

  return answer;
}
