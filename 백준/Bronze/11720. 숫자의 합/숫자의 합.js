const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

const [_, number] = input;
let sum = [...number].reduce((acc, curr) => acc + Number(curr), 0);
console.log(sum);
