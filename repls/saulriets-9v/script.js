window.addEventListener("load", () => {
  let long
  let lat
  let rietaLaiks = document.getElementById('rezultats')
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(position => {
      long = position.coords.longitude;
      lat = position.coords.latitude;
      // alert("tu esi koordinātēs " + long +" un "+ lat)
      fetch("https://api.sunrise-sunset.org/json?lat=${lat}&lng=${long}&date=today")
        .then(response => {return response.json()})
        .then(data => {
          console.log(data)
          let rietaLaiksNoAPI = data.results.sunset
          rietaLaiks.textContent = rietaLaiksNoAPI
        })
    })
  }
})