function math() {
  let a = Number(document.getElementById("a").value);
  let b = Number(document.getElementById("b").value);
  
  document.getElementById("sum").innerHTML = a +"+"+b+"="+(a+b);
  document.getElementById("minus").innerHTML = a +"-"+b+"="+(a-b);
  document.getElementById("reiz").innerHTML = a +"×"+b+"="+(a*b);
}