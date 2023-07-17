const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";

let input = fs.readFileSync(filePath).toString().split("\n");
let [nm, A, B] = input;
let [n, m] = nm.split(" ");
let i = 0;
let j = 0;
let answer = [];
let arrA = A.split(" ").map((ele) => Number(ele));
let arrB = B.split(" ").map((ele) => Number(ele));

while (i < n && j < m) {
  if (arrA[i] < arrB[j]) {
    answer.push(arrA[i++]);
  } else {
    answer.push(arrB[j++]);
  }
}
if (i < n) {
  answer = answer.concat(arrA.slice(i));
}
if (j < m) {
  answer = answer.concat(arrB.slice(j));
}
console.log(answer.join(" "));
