async function saraksts() {
  let klasesDati = await fetch("9b.txt")
  let dati = await klasesDati.text(); //nolasa failu kā tekstu
  let saraksts = dati.split("\n"); //sadala tekstu sarakstā, kur katrs ieraksts ir jauna rinda
  let html = "<h1>9.B klases skolēni</h1>"; //izveido hvirsrakstu
  html += "<ol> "; //izveido sarakstu
  for (let i = 0; i < saraksts.length; i++) {
    html += "<li>" + saraksts[i] + "</li>"; //pievieno sarakstam elementus
  }
    html += "</ol> "; //noslēdz sarakstu
html +="<h1>Sajaukts saraksts</h1>";
saraksts.sort(() => Math.random() - 0.5); //sajauc sarakstu
html += "<ol>"; //izveido sarakstu
while (saraksts.length){
  html += "<li>" + saraksts.splice(0,4).join(", ") + "</li>"; //pievieno sarakstam elementus pa 4 reizē
}
  html += "</ol> "; //noslēdz sarakstu  
document.body.innerHTML += html; //ieraksta html vērtību lapā 
}