let x = 1;
function f2(y = x){
  let x = 2;
  console.log(y);
}

f2(8)
console.log("-----");
f2()