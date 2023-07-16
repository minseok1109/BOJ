const input = require("fs").readFileSync("/dev/stdin").toString();

function factorize(number) {
  const factors = [];

  while (number % 2 === 0) {
    factors.push(2);
    number /= 2;
  }

  let divisor = 3;
  let sqrt = Math.sqrt(number);
  while (divisor <= sqrt) {
    if (number % divisor === 0) {
      factors.push(divisor);
      number /= divisor;
      sqrt = Math.sqrt(number);
    } else {
      divisor += 2;
    }
  }

  if (number > 1) {
    factors.push(number);
  }

  return factors;
}

let answer = factorize(input);
answer.map((item) => console.log(item));
