let c = [2320956, 2299390, 2276520, 2249724, 2227874, 2208840, 2191910, 2162834, 2120504, 2074605, 2044813, 2023825, 2001468, 1968957, 1950116, 1934379, 1919968, 1907675, 1893223, 1875757] // ievietoju datus ar cilvēku skaitu

let a = [840066.00, 982066.00, 1136739.00, 1230621.00, 1420459.00, 1386568.00,1368790.00, 1033908.00,	1033908.01, 1033908.02, 1033908.03, 1033908.04, 1033908.05, 1033908.06,	1033908.07,	1033908.08, 1033908.09,	1033908.10, 1033908.11, 1033908.12,	1033908.13] // ievietoju datus ar atkritumu daudzumu
let slider = document.getElementById("slidnis"); // ievietoju slīdni
let output = document.getElementById("atrums"); 
output.innerHTML = slider.value;
slider. oninput = function()  {
  output. innerHTML = this.value + ". gads";
  document.getElementById("skaits").innerHTML = c[this.value-2002] + " cilvēki"; //rādu to ierakstu kurš sarakstā atbilst ar slīdni
  document.getElementById("atkritumi").innerHTML = a[this.value-2002] + " tonnas"; // rādu to ierakstu kurš sarakstā atbilst ar slīdni
}