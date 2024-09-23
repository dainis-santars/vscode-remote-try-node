const API = "https://hidden-chat-test.dainisantars.repl.co"

let zinas = document.querySelector('.chataZinas');

function sutitZinu()
{
    // console.log('sutitZinu() Darbojas');
    zinas.innerHTML = zinas.innerHTML + '<br />' + zina.value;
    fetch(API + '/sutit/' + zina.value)
}

async function ieladetChataZinas()
{
    let datiNoServera = await fetch(API + '/lasit');
    let dati = await datiNoServera.text();
    zinas.innerHTML = dati;
}

//setInterval( ieladetChataZinas, 1000 )

async function ieladetChataZinasJson()
{
    let datiNoServera = await fetch(API + '/lasit');
    let dati = await datiNoServera.json();
    zinas.innerHTML = '';
    i = 0;
    while ( i < await dati.length )
    {
        zinas.innerHTML = zinas.innerHTML + i + "/" + dati[i]['zina']+'&lowast;&nbsp;';
        i = i+1;
    }
}
setInterval(ieladetChataZinasJson,1000)