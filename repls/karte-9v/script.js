window.addEventListener("load", () => {
  let long
  let lat
  let rietaLaiks = document.getElementById('rezultats')
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(position => {
      long = position.coords.longitude;
      lat = position.coords.latitude;
      // alert("tu esi koordinātēs " + long +" un "+ lat)
      let map = L.map('map').setView([lat, long], 13);
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
maxZoom: 19,
attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
var marker = L.marker([lat, long]).addTo(map);
    })
  }
})