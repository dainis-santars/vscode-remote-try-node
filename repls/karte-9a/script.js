window.addEventListener("load", () => {
  let long
  let lat
  let rietaLaiks = document.querySelector('.rezultats')
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(position => {
      long = position.coords.longitude;
      lat = position.coords.latitude;
      var map = L.map('map').setView([56.69437,23.76386], 16);
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map);
      var marker = L.marker([56.69437,23.76386]).addTo(map);
    })
  }
})