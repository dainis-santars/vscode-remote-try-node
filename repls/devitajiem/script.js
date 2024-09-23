function math() {
  let a = Number(document.getElementById('a').value);
  let b = Number(document.getElementById('b').value);

  document.getElementById("sum").innerHTML = a + " + " + b + " = " + (a + b);
  document.getElementById("strp").innerHTML = a + " - " + b + " = " + (a - b);

}
