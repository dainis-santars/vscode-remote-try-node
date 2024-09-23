// http://api.farmsense.net/v1/moonphases/?d=1681825430


window.addEventListener("load", () => {
  let long
  let lat
  let rietaLaiks = document.querySelector('.rezultats')
   if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(position => {
      
      long = position.coords.longitude;
      lat = position.coords.latitude;

      fetch(`https://api.sunrise-sunset.org/json?lat=${lat}&lng=${long}&date=today&formatted=0`)
        .then(response => {return response.json()})
        .then(data => {
          console.log(data);
          const rietaLaiksNoAPI = data.results.sunset;
          let date = new Date(rietaLaiksNoAPI);
          rietaLaiks.textContent = ("Šodien,  "+date.getDate()+
          "."+(date.getMonth()+1)+
          "."+date.getFullYear()+
          ", saule rietēs plkst. "+date.getHours()+
          "."+date.getMinutes());
        });
    });
  }
});