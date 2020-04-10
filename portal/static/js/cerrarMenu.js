let botonInicio = document.getElementById("botonNavInicio");
let botonAboutUs = document.getElementById("botonAboutUs");
let botonContacto = document.getElementById("botonNavContacto");

function esconderNav() {

    if (screen.width < 995) {
        let nav = document.getElementById("navbarSupportedContent");
        if (nav !== "") {
            nav.className = ('navbar-collapse barraNav collapse');
        }
    }
};


botonInicio.addEventListener("click", function() {
    esconderNav();
});

botonAboutUs.addEventListener("click", function() {
    esconderNav();
});

botonContacto.addEventListener("click", function() {
    esconderNav();
});