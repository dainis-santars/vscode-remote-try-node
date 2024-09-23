function nolasitVertibu() {
let meitenite = document.getElementById("mtn").value;
let zens = document.getElementById("zns").value;
document.getElementById("radiMeiteni").innerHTML = 'Meitene: ' + meitenite;
document.getElementById("radiZenu").innerHTML = 'Zēns: ' + zens;
document.getElementById("cipars").innerHTML =
Math.floor(Math.random() * 101) + '% mīl!';
}