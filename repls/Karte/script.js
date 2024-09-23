window.addEventListener("load", () => {
  let long
  let lat
   if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(position => {
      
      long = position.coords.longitude;
      lat = position.coords.latitude;
      // alert("esi te " + long + ", " + lat)
      
      let map = L.map('map').setView([lat,long], 13);
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map);
      let marker = L.marker([lat, long]).addTo(map);
      var circle = L.circle([lat, long], {
        color: '#333',
        fillColor: 'green',
        fillOpacity: 0.3,
        radius: 1000
      }).addTo(map);
    });
  }
});