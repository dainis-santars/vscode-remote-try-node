document.getElementById("met").addEventListener("click", roll)
function roll() {
  let cipars = Math.floor(Math.random() * 6) + 1;
  document.getElementById("bilde").innerHTML = '<img src="dice'+cipars+'.png">';
}