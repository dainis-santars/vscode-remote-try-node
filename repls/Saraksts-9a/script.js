async function saraksts() { //definēju funkciju, kas prot sagaidīt atbildi (async)
  let klasesDati = await fetch("9a.txt"); //pieslēdzos failam 9a.txt
  let dati = await klasesDati.text(); //nolasa faila saturu kā tekstu
  let arr = dati.split("\n"); //sadala tekstu pēc "enter" un izveido sarakstu
 // alert(arr); // parāda sarakstu lodziņā
  let html = "<h1>9.a klases skolēni</h1>"; //izveido virsrakstu html lapā"
  html += "<ol>"; //izveido sarakstu html lapā
   for(let i=0; i<arr.length; i++){
     html += "<li>"+arr[i]+"</li>";
   }
  html += "</ol>";
  html += "<h1>Sajaukts saraksts</h1>";
  html += "<ol>";
  // const sajaukts = arr.sort((b, a) => 0.5 - Math.random());
  // while (sajaukts.length) {
  //    html += "<li>grupa: " + sajaukts.splice(0,3).join(", ") + "</li>";
  // }
  for (let i = arr.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
    }
// alert(arr);
  while (arr.length) {
     html += "<li>grupa: " + arr.splice(0,4).join(", ") + "</li>";
  }
  html += "</ol>";
  document.body.innerHTML += html;
}