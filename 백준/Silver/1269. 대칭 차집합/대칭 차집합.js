const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";

let input = fs.readFileSync(filePath).toString().split("\n");

let [n, A, B] = input;
let arrA = new Set(A.split(" "));
let arrB = new Set(B.split(" "));

function difference(setA, setB) {
  const _difference = new Set(setA);
  for (const elem of setB) {
    _difference.delete(elem);
  }
  return _difference;
}

let a_b = difference(arrA, arrB);
let b_a = difference(arrB, arrA);
console.log(a_b.size + b_a.size);
