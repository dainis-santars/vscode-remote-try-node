

// https://api-saule.dainisantars.repl.co/script.js



window.addEventListener("load", () => {
  let long
  let lat
  let rietaLaiks = document.querySelector('.rezultats')
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(position => {
      long = position.coords.longitude;
      lat = position.coords.latitude;
      //alert("tu esi koordinātēs" + long + lat)
      var map = L.map('map').setView([lat, long], 13);
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
maxZoom: 19,
attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
var marker = L.marker([lat, long]).addTo(map);
var circle = L.circle([lat, long], {
color: 'red',
fillColor: '#00ff00',
fillOpacity: 0.2,
radius: 1000
}).addTo(map);

    })
  }
})