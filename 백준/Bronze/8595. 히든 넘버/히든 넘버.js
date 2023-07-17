const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

let [n, number] = input;

const numbers = number.match(/\d+/g);
let answer = 0;
if (numbers) {
  answer = numbers.reduce((acc, curr) => (acc += Number(curr)), 0);
}
console.log(answer);
