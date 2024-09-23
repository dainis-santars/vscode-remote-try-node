async function dalisanaGrupas()
{
    let klasesDati = await fetch('8a.txt');
    let dati = await klasesDati.text();
    let arr = dati.split('\n');
    document.write("<ol>")
    for (i = 0; i < arr.length; i++)
      document.write("<li>" + arr[i]) + "</li>";
    document.write("</ol>")
    document.write("<h1>Grupas</h1>")
    document.write("<ol>")
  arr.sort(() => Math.random() - 0.5);
  while(arr.length) {
    document.write("<li>grupa:&nbsp;" + arr.splice(0,3).join(', ') + "</li>");
}
  document.write("</ol>")
}
// //https://www.freecodecamp.org/news/javascript-split-how-to-split-a-string-into-an-array-in-js/
//https://www.w3docs.com/snippets/javascript/how-to-randomize-shuffle-a-javascript-array.html
// https://stackoverflow.com/questions/13939573/how-to-add-spaces-between-array-items-javascript
//https://stackoverflow.com/questions/7273668/how-to-split-a-long-array-into-smaller-arrays-with-javascript