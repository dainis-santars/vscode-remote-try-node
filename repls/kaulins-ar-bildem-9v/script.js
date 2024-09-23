document.getElementById("met").addEventListener("click", izkritaCipars);
function izkritaCipars() {
  let kaulins = (Math.floor(Math.random()*6))+1;
  let bilde = document.getElementById("bilde");
  let img = document.createElement("img");
  img.src = "dice" + kaulins + ".png";
  bilde.appendChild(img);
}