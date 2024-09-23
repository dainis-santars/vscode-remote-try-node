async function temperatura() {
  let merijumuDati = await fetch('merijumi.txt');
  let dati = await merijumuDati.text();
  let arr = dati.split('\n').map(Number);
  document.getElementById("stats").style.display = "block";
  document.getElementById("temperaturas").innerHTML = (arr).join("; ");
  let skaits = arr.length;
  document.getElementById("skaits").innerHTML = skaits;
  let maxTemp = Math.max(...arr);
  document.getElementById("maxTemp").innerHTML = maxTemp;
  let minTemp = Math.min(...arr);
  document.getElementById("minTemp").innerHTML = minTemp;
  let amplituda = maxTemp - minTemp;
  document.getElementById("amplituda").innerHTML = amplituda;
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  let vid = (sum / arr.length).toFixed(2);
  console.log(vid)
  document.getElementById("vid").innerHTML = vid;
  let silti = arr.filter(arr => arr > 19);
  document.getElementById("silti").innerHTML = silti.length;
  console.log(silti, silti.length)
  let datiGrafikam = [
    {
      y: arr,
      type: 'bar'
    }
  ];
  Plotly.newPlot("grafiks", datiGrafikam);
}
