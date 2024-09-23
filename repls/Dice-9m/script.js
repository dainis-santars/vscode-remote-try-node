document.getElementById("met").addEventListener("click", metiens);
function metiens() {
  document.getElementById("met").innerHTML = kaulins;
}
let kaulins = (Math.floor(Math.random() *6)) + 1

if (kaulins == 1) {
  kaulins = "Tev izkrita ⚀"
}
else if (kaulins == 2) {
  kaulins = "Tev izkrita ⚁"
}
else if (kaulins == 3) {
  kaulins = "Tev izkrita ⚂"
}
else if (kaulins == 4) {
  kaulins = "Tev izkrita ⚃"
}
else if (kaulins == 5) {
  kaulins = "Tev izkrita ⚄"
}
else {
  kaulins = "Tev izkrita ⚅"
}