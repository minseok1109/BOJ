const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";

let input = fs.readFileSync(filePath).toString().split("\n");
let [string, bomb] = input;
let bombLength = bomb.length;
let stack = [];
let reverseString = [...string].reverse();

while (reverseString.length !== 0) {
  stack.push(reverseString.pop());
  if (
    stack.length >= bombLength &&
    stack.slice(stack.length - bombLength, stack.length).join("") === bomb
  ) {
    stack.splice(stack.length - bombLength, bombLength);
  }
}

if (stack.length === 0) {
  console.log("FRULA");
} else {
  console.log(stack.join(""));
}
