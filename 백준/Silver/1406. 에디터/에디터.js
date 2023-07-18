const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";

let input = fs.readFileSync(filePath).toString().split("\n");
let [word, n, ...inputs] = input;
let lstack = [...word];
let rstack = [];

inputs.forEach((order) => {
  switch (order) {
    case "L":
      if (lstack.length) {
        rstack.push(lstack.pop());
      }
      break;
    case "D":
      if (rstack.length) {
        lstack.push(rstack.pop());
      }
      break;
    case "B":
      lstack.pop();
      break;
    default:
      let [i, n] = order.split(" ");
      lstack.push(n);
      break;
  }
});

let answer = lstack.join("") + rstack.reverse().join("");
console.log(answer);
