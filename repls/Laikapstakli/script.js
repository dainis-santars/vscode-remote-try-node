// https://api.open-meteo.com/v1/gfs?latitude=52.52&longitude=13.41&current_weather=1
// output {"latitude":52.54149,"longitude":13.359375,"generationtime_ms":1.5350580215454102,"utc_offset_seconds":0,"timezone":"GMT","timezone_abbreviation":"GMT","elevation":38.0,"current_weather":{"temperature":9.8,"windspeed":8.9,"winddirection":194.0,"weathercode":3,"time":"2023-02-15T13:00"}}
window.addEventListener("load", () => {
  let long
  let lat
  let temperatureDegree = document.querySelector('.temperatureDegree')
  // let locationTimezone = document.querySelector('.locationTimezone')
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(position => {
      
      long = position.coords.longitude;
      lat = position.coords.latitude;
      const api=`https://api.open-meteo.com/v1/gfs?latitude=${lat}&longitude=${long}&current_weather=1`;
      fetch(api)
        .then(response => {
          return response.json();
        })
        .then(data => {
          console.log(data);
          const {temperature} = data.current_weather;
          // tagad iestata elementus no API
          temperatureDegree.textContent = temperature;
        });
      
    });
  }
});