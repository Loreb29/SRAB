var com=document.getElementById("uno").textContent
var hid=document.querySelector(".egresado");
function cambio(){
    if(com=='Nombre: '){
        console.log('vaya');
        hid.classList.toggle('active');
    }
}
cambio();