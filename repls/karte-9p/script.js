window.addEventListener("load", () => {
  let long
  let lat
  let rietaLaiks = document.getElementById('rezultats')
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(position => {
      long = position.coords.longitude;
      lat = position.coords.latitude;
      //alert("Tu atrodies te: " + long + ", " + lat)
      let map = L.map('map').setView([lat, long], 13);
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map);
      let marker = L.marker([lat, long]).addTo(map).bindPopup("<img src='Jelgava.jpg' width=120>");
      let marker1 = L.marker([56.68761576818105,23.803219545995354]).addTo(map);
      var circle = L.circle([lat, long], {
        color: 'green',
        fillColor: '#ccc',
        fillOpacity: 0.5,
        radius: 1000
      }).addTo(map);

    })
  }
})