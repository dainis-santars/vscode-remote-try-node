let slider = document.getElementById("customRange1");
let output = document.getElementById("atrums");
output.innerHTML = slider.value  + " m/s";

slider.oninput = function() {
  output.innerHTML = this.value  + " m/s";
  document.getElementById("kms").innerHTML = (slider.value / 1000 * 3600).toFixed(1) + " km/h";
};
