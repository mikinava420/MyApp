import os
from kivy.app import App
from kivy.lang import Builder
print("""
DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title></title>
  <script src="https://npmcdn.com/babel-core@5.8.38/browser.min.js"></script>
  <link rel="stylesheet" href="registroIdio.css">
  <script src="registroIdio.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="jquery-3.6.0.min.js"></script>
  <style type="text/css" media="all">
  body
 {
 background-color: darkolivegreen;
}
/*.plant { 
  width: 390px;
  height: 780px;
  background-color: darkolivegreen;
}*/
#plant {
  
}
.agregar {
  display:inline-block;
  position:absolute;
  top: 300px;
  left: 170px;
  width:50px;
  height:50px;
  
  background:
    linear-gradient(#fff,#fff),
    linear-gradient(#fff,#fff),
    #000;
  background-position:center;
  background-size: 50% 2px,2px 50%; /*thickness = 2px, length = 50% (25px)*/
  background-repeat:no-repeat;
}
.radius {
  border-radius:50%;
  position: absolute;
  z-index: 3;
  top: 200px;
}
#ojoizq {
  width: 58px;
  height: 90px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.3);
  position: absolute;
  top: 350px;
  left: 130px;
  overflow: scroll;
} 
.parpadoizq {
  background: rgba(121, 150, 52, 1.5);
  border-radius: 20px;
  width: 58px;
  height: 50px;
  position: absolute;
  z-index: 4;
  top: -90px;
}
.parpadoinfizq {
  background: rgba(121, 149, 52, 1.5);
  border-radius: 20px;
  width: 58px;
  height: 55px;
  position: absolute;
  z-index: 3;
  top: 90px;
}
.pupilaizq {
  
  width: 20px;
  height: 30px;
  background-color: black;
  border-radius: 20px;
  position: absolute;
  z-index: 1;
  top: 380px;
  left: 150px;
}
.pupilader {
  width: 20px;
  height: 30px;
  background-color: black;
  border-radius: 20px;
  position: absolute;
  top: 380px;
  left: 240px;
}
.ojoder {
  width: 58px;
  height: 90px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.3);
  position: absolute;
  top: 350px;
  left: 220px;
  overflow: scroll;
} 
.parpadoder {
  background: rgba(121, 149, 52, 1.5);
  border-radius: 20px;
  width: 58px;
  height: 45px;
  position: absolute;
  top: -90px;
  z-index: 5;
  
}
.parpadoinfder {
  background: rgba(121, 149, 52, 1.5);
  border-radius: 20px;
  width: 58px;
  height: 45px;
  position: absolute;
  top: 90px;
  z-index: 6;
}
.plant1 { 
  
  width: 390px;
  height: 380px;
  background-color: darkolivegreen;
  position: absolute;
  top: -80px;
  z-index: 0;
  
  
}
.lineasContac {
  
  width: 40px;
  height: 40px;
  background-color: rgba(255, 248, 231, 0.3);
  position: absolute;
  top: 350px;
  left: 100px;
  z-index: 10;
}
.cama {
  
  width: 40px;
  height: 40px;
  background-color: rgba(255, 248, 231, 0.3);
  position: absolute;
  top: 250px;
  left: 100px;
  z-index: 10;
  
}
.textos {
  
  text-align: center;
  width: 240px;
  height: 70px;
  background-color: darkolivegreen;
  border-radius: 20px;
  border-color: rgba(121, 149, 52, 0.5);
  position: absolute;
  top: 140px;
  left: 65px;
  
  z-index: 3;
  
}
.discursos {
  text-align: center;
  width: 240px;
  height: 70px;
  background-color: darkolivegreen;
  border-radius: 20px;
  border-color: rgba(121, 149, 52, 0.5);
  position: absolute;
  top: 283px;
  z-index: 0;
  left: 65px;
  
}
.comprensionlectora {
  text-align: center;
  width: 240px;
  height: 70px;
  background-color: darkolivegreen;
  border-radius: 20px;
  border-color: rgba(121, 149, 52, 0.5);
  position: absolute;
  top: 442px;
  left: 65px;
  
}
.contenedor {
  
  background-color: darkolivegreen;
  position: absolute;
  top: 60px;
  left: 25px;
  border-radius: 20px;
  width: 350px;
  height: 200px;
}
.navegadorResumen {
  width: 350px;
  height: 30px;
  background-color: darkolivegreen;
  position: absolute;
  top: -35px;
  border-radius: 20px;
  overflow: scroll;
}
.descriptivo {
  width: 130px;
  height: 30px;
  background: darkolivegreen;
  position: absolute;
  top: 1px;
  text-align: center;
  color: darkolivegreen;
}
.informativo {
  width: 130px;
  height: 30px;
  background: darkolivegreen;
  position: absolute;
  top: 1px;
  left: 130px;
  text-align: center;
  color: darkolivegreen;
  
}
.investigativo {
  width: 130px;
  height: 30px;
  background: darkolivegreen;
  position: absolute;
  top: 1px;
  left: 265px;
  text-align: center;
  color: darkolivegreen;
  
}
.sinopsis {
  width: 130px;
  height: 30px;
  background: rgba(255, 248, 231, 0.3);
  position: absolute;
  top: 1px;
  left: 395px;
  text-align: center;
}
.desliz1 {
  width: 350px;
  height: 5px;
  background-color: darkolivegreen;
  position: absolute;
  top: 287px;
  
}
.start {
  width: 80px;
  height: 40px;
  background: rgba(211, 211, 211, 0.3);
  position: absolute;
  top: 240px;
  display: none;
}
.navegadorMapaMental {
  display: none;
  width: 350px;
  height: 80px;
  background-color: rgba(255, 248, 231, 0.3);
  position: absolute;
  top: 290px;
  left: 30px;
  border-radius: 20px;
  overflow: scroll;
  
}
.mapaMen {
  width: 150px;
  height: 60px;
  border-radius:20px;
  background-color: darkolivegreen;
  position: absolute;
  top: 10px;
  left: 12px;
}
.mapaCon {
  width: 150px;
  height: 60px;
  border-radius:20px;
  background-color: darkolivegreen;
  position: absolute;
  top: 10px;
  left: 175px;
}
.llaves {
  width: 150px;
  height: 60px;
  border-radius:20px;
  background-color: darkolivegreen;
  position: absolute;
  top: 10px;
  left: 338px;
}
.lluvia {
  width: 150px;
  height: 60px;
  border-radius:20px;
  background-color: darkolivegreen;
  position: absolute;
  top: 10px;
  left: 505px;
}
.contenedor2 {
  width: 350px;
  height: 80px;
  background-color: rgba(255, 248, 231, 0.3);
  position: absolute;
  top: 140px;
  left: 20px;
  
  
}
.contene {
 display: none;
  width: 350px;
  height: 200px;
  border-radius: 20px;
  position: absolute;
  top: 400px;
  left: 30px;
  background: rgba(255, 248, 231, 0.3);
  
}
.respuesta {
  display: none;
  width: 350px;
  height: 40px;
  border-radius: 20px;
  position: absolute;
  top: 630px;
  left: 23px;
  background: rgba(255, 248, 231, 0.3);
  
}
.respuesta2 {
  display: none;
  width: 350px;
  height: 40px;
  border-radius: 20px;
  position: absolute;
  top: 700px;
  left: 25px;
  background: rgba(255, 248, 231, 0.3);
  
}
   
  </style>
</head>

<body>
  
  <div class="plant" id="plant"></div>
 <!-- <div class="agregar" id="agregar"></div>
    <div class="agregar radius" id="radius"></div> !-->
  <div class="ojoizq" id="ojoizq">
    <div class="parpadoizq" id="parpadoizq"></div>
    <div class="parpadoinfizq" id="parpadoinfizq"></div>
  </div>  
  <div class="pupilaizq" id="pupilaizq"></div>
  <div class="ojoder" id="ojoder">
    <div class="parpadoder" id="parpadoder"></div>
    <div class="parpadoinfder" id="parpadoinfder"></div>
  </div>
  <div class="pupilader" id="pupilader"></div>
  <div class="plant1" id="plant1"></div>
  <div class="lineasContac">
    <div class="lin1"></div>
    <div class="lin2"></div>
    <div class="lin3"></div>
  </div>
  <!--<div class="cama"></div> -->
  <div class="textos" id="textos"></div>
  <div class="discursos" id="discursos"></div>
  <div class="comprensionlectora" id="comprensionlectora"></div>
  <div class="contenedor" id="contenedor">
    <div id="fleDeree"></div>
    <div id="fleIzq"></div>
    <div class="navegadorResumen" id="navegadorResumen">
       <div class="descriptivo" id="descriptivo">descriptivo</div>
       <div class="informativo" id="informativo">informativo</div>
       <div class="investigativo" id="investigativo">investigativo></div>
       <div></div>
      
    </div>
    <div class="desliz1" id="desliz1"></div>
    <div class="recorrdesliz" id="recorrdesliz"></div>
  </div>
  <div class="navegadorMapaMental">
    <div class="mapaMen">Mental</div>
    <div class="mapaCon">Conceptual</div>
    <div class="llaves">cuadro-sinoptico</div>
    <div class="lluvia">lluvia</div>
    <diclass="barr"></div>
  </div>
  <div id="start" class="start"></div>
  <div class="contene" id="contene">
    <div id="categoria"></div>
    <img src="">
  </div>
   <div class="respuesta" id="respuesta"></div>
    <div class="respuesta2" id="respuest2"></div>
    <div class="respuesta3" id="respuesta3"></div>
  <script type="text/javascript">
  window.onload = function() {
//  agregarPr();
descrip();
cam();
cargarDomPregun();
abrirYCerrarOjos();
primCam();
escogModo1();
}

/*function agregarPr () {
  var agregar = document.getElementById('agregar');
  
  agregar.addEventListener('click', cambiar, false);
  
  function cambiar () {
    
   var disAgre = document.createElement('p');
   var texAgre = 'Agrega tareas y gana seguidores';
   var textoAgre = document.createTextNode(texAgre);
    disAgre.style.width = '350px';
    disAgre.style.height = '290px';
    
    disAgre.style.display = ' ';
    disAgre.style.background = 'rgba(155, 248, 231, 0.3';
    disAgre.appendChild(textoAgre);
    var contene = document.getElementById('contenedor');
    contene.appendChild(disAgre);
     
    
  }
 
}
*/
function abrirYCerrarOjos () {
  function cerrar () {
    let parpadoSup = document.getElementById('parpadoizq');
    let parpadoInf = document.getElementById('parpadoinfizq');
    let parpadoSupDer = document.getElementById('parpadoder');
    let parpadoInfDer = document.getElementById('parpadoinfder');
  
    parpadoSupDer.style.top = '5px';
    parpadoInf.style.top = '40px';
    parpadoSup.style.top = '3px';
    parpadoInfDer.style.top = '43px';
    
  }
  function abrir () {
    let parSupIzq = document.getElementById('parpadoizq');
    let parInfIzq = document.getElementById('parpadoinfizq');
    let parSupDer = document.getElementById('parpadoder');
    let parInfDer = document.getElementById('parpadoinfder')
    parSupDer.style.top = '-17px';
    parInfIzq.style.top = '55px';
    parSupIzq.style.top = '-17px';
    parInfDer.style.top = '54px';
    
    
    
  }
  var inter = setInterval(cerrar, 1000);
  var inter2 = setInterval(abrir, 2500);
}
function primCam () {
  var primCmb = document.getElementById('plant');
  primCmb.addEventListener('click', camb1, false);
  
  function camb1 () {
    let ojoder = document.getElementById('ojoder');
    let ojoizq = document.getElementById('ojoizq');
    let pupilaIzq = document.getElementById('pupilaizq');
    let pupilaDer = document.getElementById('pupilader');
    
    pupilaDer.style.display = 'none';
    ojoder.style.display = 'none';
    ojoizq.style.display = 'none';
    pupilaIzq.style.display = 'none';
    
    let textos = document.getElementById('textos');
    let discursos = document.getElementById('discursos');
    let comprension = document.getElementById('comprensionlectora');
    
    textos.style.background = "rgba(255, 248, 231, 0.3)";
    discursos.style.background = 'rgba(255, 248, 231, 0.3)';
    comprension.style.background = 'rgba(255, 248, 231, 0.3)';
   /* let explica = document.createElement('p');
    
    explica.innerHTML = 'Bienvenido';
    explica.style.width = '30px;'
    explica.style.color = 'white';
    explica.style.position = 'absolute';
    explica.style.zIndex = '8';
    explica.style.top = '300px';
    explica.style.background = 'rgba(255, 248, 231, 0.3)';
     explica.style.display = ' ';
     let body = document.body.appendChild(explica);*/
    
    
  }
}

function escogModo1 () {
  var segCmb = document.getElementById('textos');
  segCmb.addEventListener('click', segCam, false);
  function segCam () {
    let explica = document.createElement('p');
    
    explica.innerHTML = 'Bienvenido';
    explica.style.width = '30px;'
    explica.style.color = 'white';
    explica.style.position = 'absolute';
    explica.style.zIndex = '8';
    explica.style.top = '700px';
    explica.style.background = 'rgba(255, 248, 231, 0.3)';
     explica.style.display = ' ';
     let body = document.body.appendChild(explica);
    let textos = document.getElementById('textos');
    let discursos = document.getElementById('discursos');
    let comprension = document.getElementById('comprensionlectora');
    let contenedor = document.getElementById('contenedor');
    textos.style.display = 'none';
    discursos.style.display = 'none';
    comprension.style.display = 'none';
    contenedor.style.background = 'rgba(255, 248, 231, 0.3)';
    let navegaResu = document.getElementById('navegadorResumen');
    navegaResu.style.background = 'rgba(180, 165, 129, 0.3)';
    let descriptiv = document.getElementById('descriptivo');
    descriptiv.style.background = ' rgba(255, 248, 231, 0.3)';
    descriptiv.style.color = 'black';
    let informativ = document.getElementById('informativo');
    informativ.style.background = 'rgba(255, 248, 231, 0.3)';
    informativ.style.color = 'black';
    let investigativ = document.getElementById('investigativo');
    investigativ.style.backgroundColor = 'rgba(255, 248, 231, 0.3)';
    investigativ.style.color = 'black';
    let desliz1 = document.getElementById('desliz1');
    desliz1.style.background = 'black';
    
    var obten = navigator.mediaDevices.getUserMedia({audio: true, video: true})
    
     
  }
}
function descrip () {
  var descriptivo = document.getElementById('descriptivo');
  descriptivo.addEventListener('click', descri, false);
  
  function descri () {
    
    
    var fleDere = document.getElementById('fleDeree');
    
    fleDere.style.width = '30px';
    fleDere.style.height = '30px';
    fleDere.style.backgroundColor = 'linen';
    fleDere.style.borderRadius = '20px'
    fleDere.style.position = 'absolute';
    fleDere.style.display = ' ';
    fleDere.style.position = 'absolute';
    fleDere.style.left = '300px';
    fleDere.style.top = '100px';
    
    var fleIzq = document.getElementById('fleIzq')
    fleIzq.style.width = '30px';
    fleIzq.style.height = '30px';
    fleIzq.style.backgroundColor = 'linen';
    fleIzq.style.borderRadius = '20px'
    fleIzq.style.position = 'absolute';
    fleIzq.style.display = ' ';
    
    
    var des = document.getElementById('contenedor');
    des.appendChild(fleDere);
    des.appendChild(fleIzq);
    
  
    
  }
  
}
var text = {
  categoria: ["Resumen descriptivo", "Resumen informativo"],
  pregunta:"¿cuales son los tipos de texto?",
  respuesta: "Referencial, apelativo, poetico",
  respuesta2: "Argumentativo, Narrativo, Descriptivo",
  respuesta3: "argumentativo, referencial, narrativo",
  imagen: "https://images.app.goo.gl/5Q9gKarvrUaNcheTA",
  
  
  imprimir: function () {
    
  }
};

var contene = document.getElementById('contene');
var cate = document.getElementById('categoria');


function cargarDomPregun () {
  let startt = document.getElementById('start');
  startt.addEventListener('click', empe, false);
}
function empe () {
  let start1 = document.getElementById('start');
  start1.style.display = 'none';
  
}

escogerPregun(0);
function escogerPregun () {
 let preguntas = lectura("preguntasRegustruIdio.json");
 let interPre = JSON.parse(preguntas);
 
 
  
}
function lectura (ruta_local) {
  var lec = new XMLHttpRequest();
  lec.open('GET', ruta_local, false);
  lec.send();
  
  
}
var cont;
function cam () {
      var fleDe = document.getElementById('fleDeree');
      fleDe.addEventListener('click', dere, false);
      
      function dere () {
        
        var texto = document.createElement('p');
        
        texto.style.display = ' ';
        let recorCamGuar = 0;
        let recorCam;
        
        for(recorCam=0; recorCam<=text.categoria.length; recorCam++) {
           recorCamGuar = recorCam;
           var textt = document.createTextNode(text.categoria[recorCamGuar]);
          ;
        }
        
        texto.appendChild(textt);
        var dess = document.getElementById('contenedor');
        dess.appendChild(texto);
      }
    }
function cam2 () {
      var fleIzq = document.getElementById('fleIzqq');
      fleIzq.addEventListener('click', izq, false);
      
      function izq () {
        var textoo = document.createElement('p');
        var textt = document.createTextNode(text[0]);
        textoo.appendChild(textt);
        des.appendChild(textoo)
       
      }
    }
 
  </script>

</body>

</html>
""")

os.system("touch file.png")