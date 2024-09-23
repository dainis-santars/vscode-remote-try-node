var slider = document.getElementById("diapazons");
var slider2 = document.getElementById("diapazons2");
var slider3 = document.getElementById("diapazons3");
var output = document.getElementById("krasa");
var output2 = document.getElementById("krasa2");
var output3 = document.getElementById("krasa3");

slider.addEventListener("input", updateColor);
slider2.addEventListener("input", updateColor);
slider3.addEventListener("input", updateColor);

slider.oninput = function() {
  output.innerHTML = this.value + " sarkans";
}
slider2.oninput = function() {
  output2.innerHTML = this.value + " zaļš";
}
slider3.oninput = function() {
  output3.innerHTML = this.value + " zils";
}

function updateColor() {
  var newColor = `rgb(${slider.value},${slider2.value},${slider3.value})`;
  document.getElementById("krasainaisLaukums").style.backgroundColor = newColor;
}