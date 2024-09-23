function loveMeter() {
  let meitene = document.getElementById('m').value;
  document.getElementById("meitene").innerHTML = meitene;
  let puisis = document.getElementById('p').value;
  document.getElementById("puisis").innerHTML = puisis;
  document.getElementById("cipars").innerHTML =   Math.floor(Math.random() * 101) + "% love 💕💕💕"
}