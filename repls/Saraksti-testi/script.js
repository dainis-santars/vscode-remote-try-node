async function dalisanaGrupas() {
  let skaits = document.getElementById('skaits').value
  let klasesDati = await fetch('8a.txt');
  let dati = await klasesDati.text();
  let arr = dati.split('\n');
  let saraksts = "";
  let grupas = "";
  for (let i = 0; i < arr.length; i++) {
    saraksts += "<li>" + arr[i] + "</li>";
  }
  document.getElementById("skoleni").innerHTML = saraksts;

  arr.sort(() => Math.random() - 0.5);
  // console.log(arr);
  while(arr.length) {
    grupas += "<li>" + arr.splice(0, skaits).join(', ') + "</li>";
  }
  document.getElementById("grupas").innerHTML = grupas;
  // let r = arr.filter(arr => arr.length > 18);
  // console.log(r)
}
