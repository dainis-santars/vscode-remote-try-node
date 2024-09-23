let slider = document.getElementById("diapazons");
let output = document.getElementById("atrums");
output.innerHTML = slider.value + " m/s";


slider.oninput = function() {
  output.innerHTML = this.value + " m/s";
  document.getElementById("kms").innerHTML = (slider.value * 3.6).toFixed(1) + " km/h"
}