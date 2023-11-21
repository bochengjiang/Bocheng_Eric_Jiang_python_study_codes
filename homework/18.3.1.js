var x = 1;
function f1(x, y = x) {
  console.log(y);
}

f1(8)
console.log("-----");
f1()