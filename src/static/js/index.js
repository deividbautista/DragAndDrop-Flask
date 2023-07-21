//------------------------------------------------------------------------------------
// El presente código posee la finalidad de aprender y practicar conocimientos intermedios 
// del lenguaje de programación "JavaScripts" y "Python" con el framework "Flask", en ningún momento se pretende monetizar o 
// hacer apropiación del trabajo del autor en el que se inspira el diseño y parcialmente la codificación.
//------------------------------------------------------------------------------------
// Código y diseño inspirado del canal: Vida MRR - Programacion web "https://www.youtube.com/@vidamrr" 
// link-video: https://youtu.be/qWFwYLUGWrc
// link-repositorios: https://github.com/marcosrivasr/Curso-de-NodeJS 

let archivosSeleccionados = [];
const button = document.querySelector(".botonArchivos");
const inp = document.querySelector("#fileInput");
const dropArea = document.querySelector(".dropArea");
const dragText = dropArea.querySelector("h2");


button.addEventListener('click', e => {
    inp.click();
    console.log("wenas")
});

inp.addEventListener("change", (event) => {
    event.preventDefault();
    archivosSeleccionados.push(...inp.files);
    mostrarArchivos();
});

//---------------------------------------
dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("activate");
    dragText.textContent = "Suelta el archivo para subirlo ʕ•́ᴥ•̀ʔっ♡"
});

//--------------------------
dropArea.addEventListener("dragleave", (e) => {
    e.preventDefault();
    dropArea.classList.remove("activate");
    dragText.textContent = "Arrastra un archivo UwU"
});

//--------------------------
dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    archivosSeleccionados.push(...e.dataTransfer.files);
    mostrarArchivos();
    dropArea.classList.remove("activate");
    dragText.textContent = "Arrastra un archivo UwU"
});

//---------------------------------------------------------------------------------

function cerrar() {
    const closeButtons = document.querySelectorAll('.Cerrar');
    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const fileContainer = button.closest('.file-container');
            const span = fileContainer.querySelector('.name-img');
            const nombreElemento = span.textContent;
            
            const index = archivosSeleccionados.findIndex(elemento => elemento.name === nombreElemento);
            if (index !== -1) {
            archivosSeleccionados.splice(index, 1);
            fileContainer.remove();
            }
            console.log("Qué onda?")
            console.log(archivosSeleccionados);
        });
    });
}
//---------------------------------------

// function dragOverHandler(event) {
//     event.preventDefault();
//   }

// function dropHandler(event) {
//   event.preventDefault();
//   archivosSeleccionados.push(...event.dataTransfer.files);
//   mostrarArchivos();
// }


function mostrarArchivos() {
    const archivosDiv = document.getElementById('archivosSeleccionados');
    archivosDiv.innerHTML = archivosSeleccionados.map(archivo => {
        const fileReader = new FileReader();
        const id = `file-${Math.random().toString(32).substring(7)}`;
        fileReader.readAsDataURL(archivo);
        fileReader.onload = () => {
            const fileUrl = fileReader.result;
            const image = `
                <div id="${id}" class="file-container">
                    <img class="imgFile" src="${fileUrl}" alt="${archivo.name}">
                    <div class="status">
                        <span id="${id}" class="name-img">${archivo.name}</span>
                        <button class="Cerrar"><i class="iconoX fa-solid fa-xmark"></i></button>
                    </div>
                </div>
            `;
            archivosDiv.innerHTML += image;
            console.log(archivosSeleccionados);
            cerrar();
        };
    }).join('');
}

function uploadFiles() {
    const formData = new FormData();
    archivosSeleccionados.forEach(archivo => {
        formData.append('archivos', archivo);
    });

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
        .then(response => response.text())
        .then(data => console.log(data))
        .catch(error => console.error('Error al subir archivos:', error));

    archivosSeleccionados = [];
    mostrarArchivos();
}