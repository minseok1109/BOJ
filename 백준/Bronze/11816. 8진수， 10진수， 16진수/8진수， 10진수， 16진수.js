const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";

let input = fs.readFileSync(filePath).toString();

if (input.startsWith("0x")) {
  console.log(parseInt(input, 16));
} else if (input.startsWith("0")) {
  console.log(parseInt(input, 8));
} else {
  console.log(parseInt(input, 10));
}
