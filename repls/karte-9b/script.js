window.addEventListener("load", () => {
  let long
  let lat
  let rietaLaiks = document.querySelector('.rezultats')
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(position => {
      long = position.coords.longitude;
      lat = position.coords.latitude;
      var map = L.map('map').setView([lat, long], 13);
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map);
// te tagad var likt marķierus!
      var marker1 = L.marker([lat, long]).addTo(map);
      marker1.bindPopup("<b>Tu atrodies te!</b>").openPopup();
    })
  }
})