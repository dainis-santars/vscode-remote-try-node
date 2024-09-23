let vd = document.querySelector('.rezultats')

window.addEventListener("load", () => {
  fetch("https://nameday.abalin.net/api/V1/today")
    .then(response => { return response.json() })
    .then(data => {
      // console.log(data)
      let datiNoAPI = data.nameday.lv // var mainīt kodu citām valstīm
      vd.textContent = datiNoAPI
    })
})