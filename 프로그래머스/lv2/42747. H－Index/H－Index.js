function solution(citations) {
  citations.sort((a, b) => b - a);
  
  let index = 0;
  while (index <= citations.length) {
    if (index + 1 <= citations[index]) {
      index++;
    } else break;
  }
  return index;
}