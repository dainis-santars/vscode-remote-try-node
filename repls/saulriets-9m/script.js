

// https://api-saule.dainisantars.repl.co/script.js



// window.addEventListener("load", () => {
//   let rietaLaiks = document.querySelector('.rezultats')
//   if(navigator.geolocation) {
//     navigator.geolocation.getCurrentPosition(position => {
//       long = position.coords.longitude;
//       lat = position.coords.latitude;
//       alert("tu esi koordinātēs " + long + " " + lat)
//       fetch("https://api.sunrise-sunset.org/json?lat=${lat}&lng=${long}&date=today")
//       .then(response => {return response.json()})
//       .then(data => {
//         console.log(data)
//         let rietaLaiksNoAPI = data.results.sunset
//         rietaLaiks.textContent = rietaLaiksNoAPI
//       })
//     })
//   }
// })

window.addEventListener("load", function() {
  var rietaLaiks = document.querySelector('.rezultats');
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var long = position.coords.longitude;
      var lat = position.coords.latitude;
      alert("tu esi koordinātēs " + long + " " + lat);
      fetch("https://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + long + "&date=today")
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        console.log(data);
        var rietaLaiksNoAPI = data.results.sunset;
        rietaLaiks.textContent = rietaLaiksNoAPI;
      });
    });
  }
});
