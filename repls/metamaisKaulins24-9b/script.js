document.getElementById("mest").addEventListener("click", kaulins)
function kaulins() {
  let kaulins = Math.floor(Math.random() * 6) + 1;
  document.getElementById("bilde").innerHTML = '<img src="dice'+kaulins+'.png">';
}