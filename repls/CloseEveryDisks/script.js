async function temp() {
  let merijumuDati = await fetch("merijumi.txt");
  let dati = await merijumuDati.text();
  let arr = dati.split("\n").map(Number);
  document.getElementById("stats").style.display="block";
  document.getElementById("temperaturas").innerHTML = (arr).join("; ");
  let skaits = arr.length;
  document.getElementById("skaits").innerHTML = skaits;
  let min = Math.min(...arr);
  document.getElementById("min").innerHTML = min;
}