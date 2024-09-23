document.getElementById("met").addEventListener("click",metiens)
function metiens() {
  document.getElementById("met").innerHTML = kaulins
}
let kaulins = Math.floor(Math.random() * 6) + 1

if (kaulins == 1) {kaulins = "⚀"}
else if (kaulins == 2) {kaulins = "⚁"}
else if (kaulins == 3) {kaulins = "⚂"}
else if (kaulins == 4) {kaulins = "⚃"}
else if (kaulins == 5) {kaulins = "⚄"}
else {kaulins = "⚅"}